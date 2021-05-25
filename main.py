from mods.netCall import runPing, traces, processors, whois, mapit
import folium 
import webbrowser
import sys

if __name__ == "__main__":
    if runPing(sys.argv[1]):
        traces(sys.argv[1])
        lotsIP = processors(sys.argv[1])
        if lotsIP:
            locations = whois(lotsIP)
        # locations = [
        #     [23,43,'Random Wats','8.7.32.1'],
        #     [54,76,'You are here','43.90.86.57'],
        # ]
        name = mapit(locations)
        webbrowser.open(name)