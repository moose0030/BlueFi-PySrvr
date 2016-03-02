#import thread
import time
import bluetooth

def broadcast():
    addrs = {}
    nearby = bluetooth.discover_devices(flush_cache=True)
    for addr in nearby:
        name = bluetooth.lookup_name(addr, 5)
        print (addr, name)
        addrs[addr] = name
    return addrs   

def listen():
	while True:
		try:
			#mode = int(raw_input())
			#if mode is 2:
			thread.start_new_thread(printOutput,())
		except ValueError:
			print ("Not a number")

def printOutput():
    count = 0
    while count < 5:
 #       time.sleep(10)
        count+=1
        print ("Added via bluetooth")

if __name__ == "__main__":
    addrs = broadcast()
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect(("7C:D1:C3:97:81:99",port))
    sock.send("Hi!")
    data = sock.recv(1024)
    print data
    sock.close()        
    #for a in addrs:
    #    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    #    sock.connect((a[0],port))
    #    sock.send("Hi!")
    #    sock.close()        
