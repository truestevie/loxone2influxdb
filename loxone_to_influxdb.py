"""Retrieve value of analogue input on Loxone miniserver and upload it to InfluxDB."""

import sys
import xml.etree.ElementTree

import requests.auth

import settings

try:
    response = requests.get(
        url=settings.GET_URL,
        auth=(settings.GET_USER, settings.GET_PASSWORD))
except requests.exceptions.ConnectionError:
    print(f"[-] {sys.exc_info()[1]} <ConnectionError>")
    sys.exit()

if response.status_code != 200:
    print(f"[-] Http get operation resulted in unexpected status code: {response.status_code}")
    sys.exit()

tree = xml.etree.ElementTree.fromstring(response.text)

if tree.attrib.get('Code') != "200":
    print(f"[-] XML parameter 'Code' has unexpected value: {tree.attrib.get('Code')}")
    sys.exit()

value = float(tree.attrib.get('value'))

print(f"[+] Retrieved value: {value}")

try:
    response = requests.post(
        url=settings.INFLUXDB_URL,
        headers={"Content-type": "text:plain"},
        data=f"{settings.INFLUXDB_DATA_PREFIX} value={value}",
        auth=(settings.INFLUXDB_USER, settings.INFLUXDB_PASSWORD),
    )
except requests.exceptions.ConnectionError:
    print(f"[-] {sys.exc_info()[1]} <ConnectionError>")
    sys.exit()

if response.status_code != 204:
    print(f"[-] Http post operation to InfluxDB resulted in unexpected status code: {response.status_code}")
    sys.exit()

print(f"[+] Influx status code: {response.status_code}")
