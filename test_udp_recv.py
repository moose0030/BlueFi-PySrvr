import socket
#This is the android app
UDP_PORT = 3034
bus = raw_input()
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind to broadcast address
sock.bind(('0.0.0.0',UDP_PORT))
print "Socket:", sock.getsockname()
count = 0
while True:
        if count == 9:
                break
	data,addr = sock.recvfrom(1024)
	print "RECEIVED MESSAGE:", data, addr
	print addr[1]
	print data
	#print "TRYING TO SEND"
	if data == "REQ":
                sock.sendto(bus,addr)
                data = ""
                while True:
                        data,addr = sock.recvfrom(1024)
                        if data != "REQ":
                                print data
                                count += 1
                                break
                        
sock.close()
