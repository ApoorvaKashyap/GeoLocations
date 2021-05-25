import subprocess
import re
import folium
import urllib
import json

def runPing(ip):
    print("Checking for internet connectivity!!")
    try:
        ping = subprocess.run('ping {} -c 10'.format(ip), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if ping.stderr:
            raise ping.stderr
    except Exception as e:
        print(e)
        print("Please resolve this error before trying again.")
        return False
    else:
        print('Connected successfully.')
        return True

def traces(ip):
    print("Now tracing your routes!!")
    try:
        tracedRoute = subprocess.run('traceroute {} > ./traces_{}.traces'.format(ip,ip), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if tracedRoute.stderr:
            raise tracedRoute.stderr
    except Exception as e:
        print(e)
        print("Please solve this error before trying again.")
    else:
        print("Route Traced Successfully")

def whois(lotsIP):
    base = "http://ipwhois.app/json/"
    locations = []
    for i,ip in enumerate(lotsIP):
        print('{}\n{}'.format(lotsIP,ip))
        if '*' in ip and i == 0:
            locations.append([0,0])
        elif '*' in ip and i > 0:
            locations.append([locations[i-1][0],locations[i-1][1]])
        else:
            urlpath = ''.join([base,str(ip)])
            print(urlpath)
            response = json.loads(urllib.request.urlopen(urlpath).read().decode())
            #locations.append([response["latitude"],response["longitude"],"{}, {}, {}".format(response["city"],response["region"],response["country"]), str(response["ip"])])
            print(response)
    print(locations)
    return locations

def mapit(locations):
    maps = folium.Map(location=[locations[int(len(locations)/2)][0],locations[int(len(locations)/2)][1]], zoom_start=2, tiles="OpenStreetMap")
    for i,ind in enumerate(locations):
        tooltip = "<i></b>{}<i></b>".format(ind[3])
        folium.Marker(location = [ind[0],ind[1]], popup="<i> <b>{}<b> </i>".format(ind[2]), tooltip = tooltip, icon=folium.Icon(icon="cloud")).add_to(maps)
    maps.save("IP Geolocator.html")
    return "IP Geolocator.html"

def processors(ip):
    print("Finding the locations:")
    try:
        with open('traces_{}.traces'.format(ip),'r') as logs:
            adresses = []
            for i,line in enumerate(logs):
                if i == 0:
                    print(str(line))
                    continue
                else:
                    adresses.append(re.findall("\d{1,3}|\*.\d{1.3}|\*.\d{1,3}|\*.\d{1,3}|\*",line))
            args = []
            for i in adresses:
                strings = ''
                if i[1] == '*':
                    strings = '* * *'
                else:
                    for j in range(1,5):
                        strings+=i[j]+'.'
                args.append(strings[0:(len(strings)-1)])
    except Exception as e:
        print(e)
        return False
    else:
        return args

if __name__ == "__main__":
    traces('8.8.8.8')
    processors('8.8.8.8')
    whois('8.8.8.8')