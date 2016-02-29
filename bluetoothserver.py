import thread
import time

def listen():
	while True:
		try:
			#mode = int(raw_input())
			#if mode is 2:
			thread.start_new_thread(printOutput,())
		except ValueError:
			print "Not a number"

def printOutput():
	count = 0
 	while count < 5:
		time.sleep(10)
		count+=1
		print "Added via bluetooth"
