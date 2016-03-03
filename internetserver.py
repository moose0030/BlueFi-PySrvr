from socket import *
import octranspo
import thread
import time
import select

def setup():
        UDP_IP = "0.0.0.0"
	UDP_PORT = 3034
	MESSAGE = "REQ"
        
	print "BROADCASTING ON PORT:", UDP_PORT
	print "MESSAGE:", MESSAGE

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.setblocking(0)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
	return sock,MESSAGE,UDP_PORT
        

def broadcast(sock,msg,port):
        while True:
                sock.sendto(msg,("255.255.255.255",port))
		ready = select.select([sock],[],[], 1)
                if ready[0]:
                        data,addr = sock.recvfrom(1024)
                        print data
                        if data == "kill":
                                break
                        result = octranspo.nextBus(data)
                        print result
                        sock.sendto(result[0],addr)
                        
	sock.close()

def printOutput():
	print "New Thread added"
	count = 0
 	while count < 5:
		time.sleep(5)
		count+=1
		print "Added via internet"

def listen(sock):
        #print "SYN+ACK --->"
        #sock.sendto("SYN+ACK",("255.255.255.255",port))
        #data,addr = sock.recvfrom(1024)
        #print data
        result = octranspo.nextBus(data)
	print result
	sock.sendto(result[0],addr)


socket,message,port = setup()
broadcast(socket,message,port)
