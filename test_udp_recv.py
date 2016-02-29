import socket
#This is the android app
UDP_PORT = 3034
bus = raw_input()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind to broadcast address
sock.bind(('0.0.0.0',UDP_PORT))
print "Socket:", sock.getsockname()
while True:
	data,addr = sock.recvfrom(1024)
	print "RECEIVED MESSAGE:", data, addr
	print addr[1]
	print data
	while True:
		#print "TRYING TO SEND"
		if data == "CONNECT:4905":
			sock.sendto(bus,addr)
			print "MESSAGE SENT"
			data = " " 
