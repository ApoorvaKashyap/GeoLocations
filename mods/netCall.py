import subprocess
import os
import datetime

def runPing(ip):
    print("Checking for internet connectivity!!")
    try:
        ping = subprocess.run('ping {} -c 10'.format(ip), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if ping.stderr:
            raise ping.stderr
    except Exception as e:
        print(e)
        print("Please resolve this error before trying again.")
    else:
        print('Connected successfully.')

def traces(ip):
    runPing(ip)
    print("Now tracing your routes!!")
    try:
        tracedRoute = subprocess.run('traceroute {} > ./traces_{}.txt'.format(ip,ip), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        if tracedRoute.stderr:
            raise tracedRoute.stderr
    except Exception as e:
        print(e)
        print("Please solve this error before trying again.")
    else:
        print("Route Traced Successfully")

if __name__ == "__main__":
    traces('8.8.8.8')