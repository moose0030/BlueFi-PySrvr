from datetime import datetime
import octranspo
import threading
from bluetooth import *

def setup():
    print "BT---INIT>>>>>>>>>>>>>>>>>>>>>"
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(5)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "BlueFi-PyPi Server",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
                       
    print "Waiting for connection on RFCOMM channel %d" % port
    print "BT---INIT--------------------<\n"
    return server_sock

def listen(server_sock):
    n = 0
    while True:
        client_sock, client_info = server_sock.accept()
        print "Accepted connection from ", client_info
        n = n + 1
        name = "IP Comms Thread #" + str(n)
        thread1 = bt_comms_thread(n,name,client_sock)
        thread1.start()

def comms(client_sock):
    try:
        while True:
            data = client_sock.recv(1024)
            print "RECEIVED [%s]" % data

            if len(data) == 0: break
            if data == 'kill':              #CLIENT KILLING SERVER
                client_sock.send("TERMINATE")
                client_sock.close()
                return
            if data == 'TEST_BT':           #CLIENT TESTING QUERY
                result = 'SUCCESS!'
            else:                           #NORMAL QUERY
                
                before = datetime.now()
                result = octranspo.nextBus(data)
                after = datetime.now()
                print "Bluetooth DB:", after - before
                with open("logs.txt","a") as logfile:
                        logfile.write("BT:"+str(after-before) + "\n")
            client_sock.send(result)
            print "SENDING  [ %s ]" % result
            
    except IOError:
        print "Error"
        return

class bt_comms_thread(threading.Thread):
    def __init__(self, threadID, name, sock):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.sock = sock

    def run(self):
        print "Starting " + self.name
        comms(self.sock)
        print "Ending " + self.name

