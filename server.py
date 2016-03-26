import internetserver
import bluetoothserver
import thread
import threading

print "this is the server"
socket,message,port = internetserver.setup()
b_server = bluetoothserver.setup()

#while True:
    #thread.start_new_thread(internetserver.broadcast,(socket,message,port,))
    #thread.start_new_thread(bluetoothserver.comms,(b_server,))
    #print thread.active



class bluetooth_thread(threading.Thread):
    def __init__(self, threadID, name, message):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.message = message

    def run(self):
        print "Starting " + self.name
        bluetoothserver.comms(b_server)
        print "Ending " + self.name

class internet_thread(threading.Thread):
    def __init__(self, threadID, name, message):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.message = message

    def run(self):
        print "Starting " + self.name
        internetserver.broadcast(socket,message,port)
        print "Ending " + self.name

thread1 = bluetooth_thread(1, "Thread BT1", "1")
thread2 = internet_thread(2, "Thread IP1", "1")
thread1.start()
thread2.start()

print "Done!"
