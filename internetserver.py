from socket import *
#import octranspo
import thread
import time

def broadcast():
	UDP_IP = "0.0.0.0"
	UDP_PORT = 3034
	MESSAGE = "CONNECT:4905"

	print "BROADCASTING ON PORT:", UDP_PORT
	print "MESSAGE:", MESSAGE

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
	sock.sendto(MESSAGE,("255.255.255.255",UDP_PORT))

	print "Socket:", sock.getsockname()

	while True:
		print "Listening:"
		data,addr = sock.recvfrom(1024)
		print "RECEIVED MESSAGE:", data		
		result = "octranspo.nextBus(data)"
		print result

def listen():
	while True:
		try:
			#mode = int(raw_input())
			#if mode is 1:
			thread.start_new_thread(printOutput,())
		except ValueError:
			print "Not a number"

def printOutput():
	#print "New Thread added"
	count = 0
 	while count < 5:
		time.sleep(5)
		count+=1
		print "Added via internet"
broadcast()
