import subprocess
import re
import folium
import urllib
import json
import random

def runPing(ip):
    print("Checking for internet connectivity!!")
    try:
        ping = subprocess.run('ping {} -c 10'.format(ip), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if ping.stderr:
            raise ping.stderr
    except Exception as e:
        print('At runping \n{}'.format(e))
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
        print('At traces \n{}'.format(e))
        print("Please solve this error before trying again.")
    else:
        print("Route Traced Successfully")

# def getInfo(url):
#     try:
#         details = subprocess.run('curl {}'.format(url), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
#         if details.stderr:
#             raise details.stderr
#     except Exception as e:
#         print(e)
#         print("Please solve this error before trying again.")
#     else:
#         print(details.stdout)
#         return details.stdout

def whois(lotsIP):
    base = "http://ipwhois.app/json/"
    locations = []
    try:
        for i,ip in enumerate(lotsIP):
            if i == 0:
                myip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf-8')
                urlpath = ''.join([base,str(myip)])
                jsonreply = urllib.request.urlopen(urlpath)
                response = json.load(jsonreply)
                locations.append([float(response["latitude"]),float(response["longitude"]),"{}, {}, {}".format(response["city"],response["region"],response["country"]), str(response["ip"])])
            elif '*' in ip and i > 0:
                locations.append([float(locations[i-1][0])+random.randint(-15,15),float(locations[i-1][1])+random.randint(-15,15),"Unknown Location","Masked IP"])
            else:
                if '172.' in ip:
                    locations.append([float(locations[i-1][0])+random.randint(-15,15),float(locations[i-1][1])+random.randint(-15,15),"Unknown Location | Private IP Range",str(ip)])
                elif '192.' in ip:
                    locations.append([float(locations[i-1][0])+random.randint(-15,15),float(locations[i-1][1])+random.randint(-15,15),"Unknown Location | Private IP Range", str(ip)])
                elif '10.' in ip:
                    locations.append([float(locations[i-1][0])+random.randint(-15,15),float(locations[i-1][1])+random.randint(-15,15),"Unknown Location | Private IP Range", str(ip)])
                else:
                    urlpath = ''.join([base,str(ip)])
                    jsonreply = urllib.request.urlopen(urlpath)
                    response = json.load(jsonreply)
                    locations.append([float(response["latitude"]),float(response["longitude"]),"{}, {}, {}".format(response["city"],response["region"],response["country"]), str(response["ip"])])
    except Exception as e:
        print('At Whois at {}\n{}'.format(i,e))
        quit()
    else:
        print("IP Geolocation successful. \nNow printing maps...")
        return locations

def mapit(locations):
    maps = folium.Map(location=[0,0], zoom_start=3, tiles="Stamen Terrain")
    for i,ind in enumerate(locations):
        tooltip = "<i></b>{}<i></b>".format(ind[3])
        folium.Marker(location = [float(ind[0]),float(ind[1])], popup="<i> <b>{}<b> </i>".format(ind[2]), tooltip = tooltip, icon=folium.Icon(icon="cloud")).add_to(maps)
        if i > 0:
            folium.PolyLine([(float(locations[i-1][0]),float(locations[i-1][1])),(float(locations[i][0]),float(locations[i][1]))]).add_to(maps)
    maps.save("IP Geolocator.html")
    print("Map Printing Successful.")
    return "IP Geolocator.html"

def processors(ip):
    print("Finding the locations:")
    adresses = []
    try:
        with open('traces_{}.traces'.format(ip),'r') as logs:
            for i,line in enumerate(logs):
                if i == 0:
                    print(str(line))
                    continue
                else:
                    if '* * *' in line:
                        adresses.append("*.*.*")
                    else:
                        adresses.append(re.search('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',line).group(1))
    except Exception as e:
        print('At Processors \n{}'.format(e))
        return False
    else:
        return adresses

if __name__ == "__main__":
    ip = ['8.8.8.8', '17.2.5.6','* * *','7.52.37.32']
    locs = whois(ip)
    name = mapit(locs)
