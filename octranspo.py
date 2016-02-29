#!/usr/bin/python
import MySQLdb

def nextBus(bus):
	# Open database
	db = MySQLdb.connect("localhost", "root","reverse","octranspo")

	# Create cursor
	cursor = db.cursor()

	# Create query
	sql = "SELECT route_id from Routes where route_short_name = " + str(bus) + ";"

	try:
	   # SQL command
	   cursor.execute(sql)
	   # Retrieve all rows
	   results = cursor.fetchone()
	   for row in results:
	      name = row[0]
	      url = row[1]
	      return results
	except:
	   return "No times were available"

	# Disconnect
	db.close()

#print nextBus(95)
