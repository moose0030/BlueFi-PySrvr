import thread
import time
import bluetooth
import octranspo

def setup():
    while True:
        clients = broadcast()
        port = 1
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        for client in clients:
            thread.start_new_thread(comms,(client, sock, port))
    return sock

def broadcast():
    addrs = {}
    nearby = bluetooth.discover_devices(flush_cache=True)
    for addr in nearby:
        name = bluetooth.lookup_name(addr, 5)
        print (addr, name)
        addrs[addr] = name
    return addrs   

def comms(client, sock, port):
    print client
    try:
        sock.connect((client,port))
        sock.send("Thank you for using SOPTS!")
        while True:
            data = sock.recv(1024)
            print data
            if data == "kill":
                break;
            result = octranspo.nextBus(data)
            sock.send(result[0])
            break
    except Exception:
        print "Exception"
        
    sock.close()   
    
socket = setup()
#comms(socket)
         
    #for a in addrs:
     #   sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    #    sock.connect((a[0],port))
    #    sock.send("Hi!")
    #    sock.close()        
