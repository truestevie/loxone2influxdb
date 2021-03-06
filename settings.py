"""Retrieve settings from settings.ini"""

from decouple import config

GET_URL = config("GET_URL")
GET_USER = config("GET_USER")
GET_PASSWORD = config("GET_PASSWORD")

INFLUXDB_URL = config("INFLUXDB_URL")
INFLUXDB_USER = config("INFLUXDB_USER")
INFLUXDB_PASSWORD = config("INFLUXDB_PASSWORD")
INFLUXDB_DATA_PREFIX = config("INFLUXDB_DATA_PREFIX")
