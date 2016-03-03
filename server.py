import internetserver
import bluetoothserver
import thread

print "this is the server"
socket,message,port = internetserver.setup()
internetserver.broadcast(socket,message,port)
