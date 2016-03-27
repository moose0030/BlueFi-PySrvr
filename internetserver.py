from socket import *
import octranspo
import time
import select
import threading

def setup():
        print "IP---INIT>>>>>>>>>>>>>>>>>>>>>"
        UDP_IP = "0.0.0.0"
	UDP_PORT = 3034
	MESSAGE = "REQ"
        
	print "BROADCASTING ON PORT:", UDP_PORT
	print "MESSAGE:", MESSAGE

	sock = socket(AF_INET, SOCK_DGRAM)
	sock.setblocking(0)
	sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sock.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
	print "IP---INIT--------------------<\n"
	return sock,MESSAGE,UDP_PORT
        

def broadcast(sock,msg,port):
        n = 0
        while True:
                sock.sendto(msg,("255.255.255.255",port))
		ready = select.select([sock],[],[], 1)
		
                if ready[0]:
                        n = n + 1
                        name = "IP Comms Thread #" + str(n)
                        thread1 = ip_comms_thread(n,name,sock)
                        thread1.start()
                        
	sock.close()
	
def comms(sock):
        try:
                data,addr = sock.recvfrom(1024)
                print "RECEIVED [ %s ]" % data
                if data == "kill":                      #CLIENT KILLING SERVER
                        sock.sendto("TERMINATE",addr)
                        sock.close()
                        return
                if data == "TEST_WIFI":                 #CLIENT TESTING QUERY
                        result = "SUCCESS!"
                else:
                        result = octranspo.nextBus(data)        #NORMAL QUERY
                print "SENDING  [ %s ]" % result
                sock.sendto(result,addr)
        except Exception:
                print "Collision with UDP"
                return

class ip_comms_thread(threading.Thread):
    def __init__(self, threadID, name, sock):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.sock = sock

    def run(self):
        print "Starting " + self.name
        comms(self.sock)
        print "Ending " + self.name
