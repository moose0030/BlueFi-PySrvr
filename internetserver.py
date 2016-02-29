import socket
import octranspo
import thread
import time

def broadcast():
	UDP_IP = "0.0.0.0"
	UDP_PORT = 3034
	MESSAGE = "CONNECT:4905"

	print "BROADCASTING ON PORT:", UDP_PORT
	print "MESSAGE:", MESSAGE

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.connect(("127.0.0.1",3034))
	sock.send(MESSAGE)

	print "Socket:", sock.getsockname()

	while True:
		print "Listening:"
		data,addr = sock.recvfrom(1024)
		print "RECEIVED MESSAGE:", data		
		result = octranspo.nextBus(data)
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
