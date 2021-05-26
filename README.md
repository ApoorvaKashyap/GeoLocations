# GeoLocations

Developed by: [Apoorva Kashyap](https://github.com/ApoorvaKashyap)

<img src="https://img.shields.io/github/last-commit/ApoorvaKashyap/GeoLocations">
<img src="https://img.shields.io/github/commit-activity/w/ApoorvaKashyap/GeoLocations">
<img src="https://img.shields.io/github/search/ApoorvaKashyap/GeoLocations/goto">
<br/>
<img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/folium" alt="folium-dependency">
<img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/urllib3">
<img src="https://img.shields.io/github/pipenv/locked/dependency-version/ApoorvaKashyap/GeoLocations/requests">

## Table of Contents

- [GeoLocations](#geolocations)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)


## Introduction

A small python program that runs the traceroute command and prints the locations of the hops on a map.

## Prerequisites

   - [ ] <b>Python 3.8.5 or later.</b> <br/>
   - Find the latest release at [Python's official site](https://www.python.org/downloads/).

   - [ ] <b> Traceroute Command </b> </br>
   - For Debian Based Distros:``` sh  sudo apt install traceroute ```</br>
   - For Windows, change the command in the [traces function](https://github.com/ApoorvaKashyap/GeoLocations/blob/master/mods/netCall.py#L25) to ```tracert```
    
   - [ ] <b> Ping Command </b>
   - Installed by default in most OSes.
