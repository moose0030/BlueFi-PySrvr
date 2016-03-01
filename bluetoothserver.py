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
    for a in addrs:
        print (a)