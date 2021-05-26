from mods.netCall import runPing, traces, processors, whois, mapit
import webbrowser
import sys

if __name__ == "__main__":
    if runPing(sys.argv[1]):
        traces(sys.argv[1])
        lotsIP = processors(sys.argv[1])
        if len(lotsIP) > 0:
            locations = whois(lotsIP)
        else:
            print("Error!!!! \nPlease try again..")
        name = mapit(locations)
        webbrowser.open(name)
        