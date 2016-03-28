import compare_time
import octranspo
from bluetooth import *

def setup():
    print "BT---INIT>>>>>>>>>>>>>>>>>>>>>"
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

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

def comms(server_sock):
    while True:
        client_sock, client_info = server_sock.accept()
        print "Accepted connection from ", client_info

        try:
            while True:
                data = client_sock.recv(1024)
                print "RECEIVED [%s]" % data

                if len(data) == 0: break
                if data == 'kill':              #CLIENT KILLING SERVER
                    client_sock.send("TERMINATE")
                    client_sock.close()
                    server_sock.close()
                    return
                    print "CLOSED SERVER"
                if data == 'TEST_BT':           #CLIENT TESTING QUERY
                    result = 'SUCCESS!'
                else:                           #NORMAL QUERY
                    result = octranspo.nextBus(data)
                client_sock.send(result)
                print "SENDING  [ %s ]" % result
                
        except IOError:
            pass
