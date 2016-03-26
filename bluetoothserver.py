import thread
import time
import octranspo
from bluetooth import *

def setup():
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(("",PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    advertise_service( server_sock, "SampleServer",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ], 
    #                   protocols = [ OBEX_UUID ] 
                        )
                       
    print "Waiting for connection on RFCOMM channel %d" % port
    return server_sock

def comms(server_sock):
    client_sock, client_info = server_sock.accept()
    print "Accepted connection from ", client_info

    try:
        while True:

            data = client_sock.recv(1024)
            print "received [%s]" % data

            if len(data) == 0: break
            if data == 'close':
                client_sock.close()
                server_sock.close()
                print "CLOSED SERVER"

            result = octranspo.nextBus(data)
            result = result + '!'
            client_sock.send(result)
            print "sent [%s]" % result
            
    except IOError:
        pass

    print "disconnected"

    client_sock.close()
    server_sock.close()
    print "all done"

server = setup()
comms(server)
