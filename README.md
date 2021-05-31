# GeoLocations

Developed by: [Apoorva Kashyap](https://github.com/ApoorvaKashyap)

<img src="https://img.shields.io/github/last-commit/ApoorvaKashyap/GeoLocations" alt="Last Commit"> &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://img.shields.io/github/commit-activity/w/ApoorvaKashyap/GeoLocations" alt="Commit Activity"> &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://img.shields.io/github/search/ApoorvaKashyap/GeoLocations/goto" alt="Goto Counter">
<br>
<img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/folium" alt="folium-dependency"> &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/urllib3" alt="urllib3-dependency"> &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/requests" alt="requests-dependency">


## Table of Contents

- [GeoLocations](#geolocations)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [How to Use](#how-to-use)
  - [Footnotes](#footnotes)


## Introduction

A small python program that runs the traceroute command and prints the locations of the hops on a map.

## Prerequisites

   - [ ] <b>Python 3.8.5 or later.</b> <br/>
   - Find the latest release at [Python's official site](https://www.python.org/downloads/).

   - [ ] <b> Traceroute Command </b> </br>
   - For Debian Based Distros:
      ```sh
      sudo apt install traceroute
      ```

   - For Windows, change the command in the [traces function](https://github.com/ApoorvaKashyap/GeoLocations/blob/master/mods/netCall.py#L25) to ``` tracert```
    
   - [ ] <b> Ping Command </b>
   - Present by default in most OSes.

   - [ ] <b>An Active Internet Connection</b>
  
## How to Use
  
  1. Download the Git Repo.
      ```sh
      git clone https://github.com/ApoorvaKashyap/GeoLocations.git
      ```
  2. Run the following commands:
      ```sh
      cd ./GeoLocations
      python3 main.py <IP Address Here>
      ```
  3. The program will run and automatically open a browser window with the hops marked.
  4. If the browser window does not open then check for ```IP Geolocator.html``` in the current working directory.
  5. The program also stores the output of the Traceroute Command in a file called ``` traces_<ip>.traces ```.

## Footnotes

1. The gateway IP address beginning of the format ```192.x.x.x``` is treated as your own location or your VPN's location and marked as such.
2. The Hidden/Masked/Private IP Adresses are marked as such and their location is taken to be ```[Previous Location's Latitude + random(-15,15), Previous Location's Longitude + random(-15,15)]```.
3. This program was primarily developed on the Ubuntu and was tested only on it. It has not yet been tested on Windows or any other platform and hence the performance is not guaranteed on platforms other than Ubuntu.
4. In accordance with Footnote 3, the ```tracert``` command is only an educated guess that may run on Windows.


<i> <b> P.S.</b> Contributions are welcome. :) So are other ideas... </i>