from mods.netCall import runPing, traces, processors, whois, mapit
import webbrowser
import sys

if __name__ == "__main__":
    if runPing(sys.argv[1]):
        traces(sys.argv[1])
        lotsIP = processors(sys.argv[1])
        if lotsIP:
            locations = whois(lotsIP)
            name = mapit(locations)
            webbrowser.open(name)
        else:
            print("Error!!!! \nPlease try again..")

        