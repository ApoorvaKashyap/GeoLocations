import subprocess
import re
import folium
import urllib
import json
import random
from rich import print
from rich.progress import Progress, SpinnerColumn, BarColumn


def progressBar():
    progress = Progress(
        SpinnerColumn("point"),
        "[progress.description]{task.description}",
        BarColumn(),
        "[magenta]{task.completed} of {task.total}",
    )
    return progress


def runPing(ip):
    print("[italic cyan]Checking for internet connectivity!!")
    try:
        with progressBar() as progress:
            task1 = progress.add_task("[italic cyan]Checking", total=5)
            for i in range(0, 5):
                ping = subprocess.run(
                    "ping {} -c 1".format(ip),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    shell=True,
                )
                progress.update(task1, advance=1)
                if ping.stderr:
                    raise ping.stderr
    except Exception as e:
        print("[bold red]At runping \n{}".format(e))
        print("[bold red]Please resolve this error before trying again.")
        return False
    else:
        print("[bold italic green]Connected successfully.")
        return True


def traces(ip):
    print("[italic cyan]Now tracing your routes!!")
    try:
        with progressBar() as progress:
            task2 = progress.add_task("[italic cyan]Tracing", total=1, start=False)
            progress.start_task(task2)
            tracedRoute = subprocess.run(
                "traceroute {} > ./traces_{}.traces".format(ip, ip),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
            )
            if tracedRoute.stderr:
                raise tracedRoute.stderr
            progress.update(task2, advance=1)
    except Exception as e:
        print("[bold red]At traces \n{}".format(e))
        print("[bold red]Please solve this error before trying again.")
    else:
        print("[bold italic green]Route Traced Successfully")


def whois(lotsIP):
    base = "http://ipwhois.app/json/"
    locations = []
    i = 0
    try:
        with progressBar() as progress:
            task3 = progress.add_task(
                "[italic cyan]Finding Locations", total=len(lotsIP)
            )
            for i, ip in enumerate(lotsIP):
                if i == 0:
                    myip = (
                        urllib.request.urlopen("https://api.ipify.org")
                        .read()
                        .decode("utf-8")
                    )
                    urlpath = "".join([base, str(myip)])
                    jsonreply = urllib.request.urlopen(urlpath)
                    response = json.load(jsonreply)
                    locations.append(
                        [
                            float(response["latitude"]),
                            float(response["longitude"]),
                            "{}, {}, {}".format(
                                response["city"],
                                response["region"],
                                response["country"],
                            ),
                            str(response["ip"]),
                        ]
                    )
                elif "*" in ip and i > 0:
                    locations.append(
                        [
                            float(locations[i - 1][0]) + random.randint(-15, 15),
                            float(locations[i - 1][1]) + random.randint(-15, 15),
                            "Unknown Location",
                            "Masked IP",
                        ]
                    )
                else:
                    if "172." in ip:
                        locations.append(
                            [
                                float(locations[i - 1][0]) + random.randint(-15, 15),
                                float(locations[i - 1][1]) + random.randint(-15, 15),
                                "Unknown Location | Private IP Range",
                                str(ip),
                            ]
                        )
                    elif "192." in ip:
                        locations.append(
                            [
                                float(locations[i - 1][0]) + random.randint(-15, 15),
                                float(locations[i - 1][1]) + random.randint(-15, 15),
                                "Unknown Location | Private IP Range",
                                str(ip),
                            ]
                        )
                    elif "10." in ip:
                        locations.append(
                            [
                                float(locations[i - 1][0]) + random.randint(-15, 15),
                                float(locations[i - 1][1]) + random.randint(-15, 15),
                                "Unknown Location | Private IP Range",
                                str(ip),
                            ]
                        )
                    else:
                        urlpath = "".join([base, str(ip)])
                        jsonreply = urllib.request.urlopen(urlpath)
                        response = json.load(jsonreply)
                        locations.append(
                            [
                                float(response["latitude"]),
                                float(response["longitude"]),
                                "{}, {}, {}".format(
                                    response["city"],
                                    response["region"],
                                    response["country"],
                                ),
                                str(response["ip"]),
                            ]
                        )
                progress.update(task3, advance=1)
    except Exception as e:
        print("[bold red]At Whois at {}\n{}".format(i, e))
        quit()
    else:
        print("[bold italic green]IP Geolocation successful.\n [/bold italic green][italic cyan]Now Printing Maps...")
        return locations


def mapit(locations):
    maps = folium.Map(location=[0, 0], zoom_start=3, tiles="Stamen Terrain")
    with progressBar() as progress:
        task4 = progress.add_task(
            "[italic cyan]Plotting Locations", total=len(locations)
        )
        for i, ind in enumerate(locations):
            tooltip = "<i></b>{}<i></b>".format(ind[3])
            folium.Marker(
                location=[float(ind[0]), float(ind[1])],
                popup="<i> <b>{}<b> </i>".format(ind[2]),
                tooltip=tooltip,
                icon=folium.Icon(icon="cloud"),
            ).add_to(maps)
            if i > 0:
                folium.PolyLine(
                    [
                        (float(locations[i - 1][0]), float(locations[i - 1][1])),
                        (float(locations[i][0]), float(locations[i][1])),
                    ]
                ).add_to(maps)
            progress.update(task4, advance=1)
    maps.save("IP Geolocator.html")
    print("[bold italic green]Map Printing Successful.")
    return "IP Geolocator.html"


def processors(ip):
    print("[italic cyan]Finding the locations:")
    addresses = []
    try:
        with open("traces_{}.traces".format(ip), "r") as logs:
            for i, line in enumerate(logs):
                if i == 0:
                    continue
                else:
                    if "* * *" in line:
                        addresses.append("*.*.*")
                    else:
                        addresses.append(
                            re.search("(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})", line).group(
                                1
                            )
                        )
    except Exception as e:
        print("[bold red]At Processors \n{}".format(e))
        return False
    else:
        return addresses


if __name__ == "__main__":
    print("[italic cyan]Please run main.py!!")
