import internetserver
import bluetoothserver
import thread
import threading

class bluetooth_thread(threading.Thread):
    def __init__(self, threadID, name, message):
        threading.Thread.__init__(self)
        self.ThreadID = threadID
        self.name = name
        self.message = message

    def run(self):
        print "Starting " + self.name
        bluetoothserver.listen(b_server)
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

print "S   O   P   T   S"
print "m   t   u   r   y"
print "a   t   b   a   s"
print "r   a   l   n   t"
print "t   w   i   s   e"
print "    a   c   i   m"
print "            t"
print "\nDeveloped by Matthew Preston"
print "------------------------------"

socket,message,port = internetserver.setup()
b_server = bluetoothserver.setup()


thread1 = bluetooth_thread(1, "BLUETOOTH SERVER THREAD", "1")
thread2 = internet_thread(2, "IP SERVER THREAD", "1")
thread1.start()
thread2.start()

print "Done!"
