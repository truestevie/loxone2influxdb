# Loxone to InfluxDB
Approach the API of a [Loxone miniserver](https://www.loxone.com) to get the value of an analogue input.
Perform a small calculation on the acquired value.
Send the resulting value to an InfluxDB.
## Retrieve value of analogue input
Use the [Loxone API](https://www.loxone.com/enen/kb/api/).
```
GET_URL=http://your_loxone/dev/sps/io/your_analogue_input/state
```
- `your_loxone` host name (or IP address) of your Loxone miniserver
- `your_analogue_input` name of the analogue input from which to get the analogue value
## Recalculate the acquired value
If needed, perform a calculation on the value that was just acquired from the miniserver.
## Send recalculated value to InfluxDB
Use the [InfluxDB API](https://docs.influxdata.com/influxdb/v1.8/guides/write_data/) to insert the calculated value in the InfluxDB.
### settings.ini   
```
INFLUXDB_URL=http://your_influxdb_server:8086/write?db=your_db
INFLUXDB_DATA_PREFIX=your_measurement,your_tag_name=your_tag_value
```
- `your_influxdb_server` host name (or IP address) of your InfluxDB server
- `your_db` name of your InfluxDB database
- `your_measurement` name of your measurement
- `your_tag_name` name of measurement tag
- `your_tag_value` value of measurement tag
 



 