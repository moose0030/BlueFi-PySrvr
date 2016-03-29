#!/usr/bin/python
import MySQLdb
from datetime import datetime
def nextBus(bus):
	# Open database
	db = MySQLdb.connect("localhost", "root","root","octranspo")

	# Create cursor
	cursor = db.cursor()

	# Create query
	bus = bus.split(':')
	time = datetime.now().time()
        time = time.replace(second = 0,microsecond =0)
	sql = "select st.arrival_time from StopTimes st, Trips t where st.stop_id in('RA900','RA905','RA915','RA910','RA920','RA925','RA940','RA945','RA950') AND t.service_id = 'EAMO15-EaMon15-Weekday-01' AND st.trip_id = t.trip_id AND t.route_id = '%s-184' AND st.arrival_time >= '%s' AND st.drop_off_type = 0 ORDER BY st.arrival_time ASC limit 1;" % (bus[0],time)

	try:
	   # SQL command
	   cursor.execute(sql)
	   # Retrieve all rows
	   results = cursor.fetchone()
	   for row in results:
	      name = row
	      return name
	except:
	   return "No times were available"

	# Disconnect
	db.close()

#print nextBus('97: Rideau Centre')
