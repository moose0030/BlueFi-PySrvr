import internetserver
import bluetoothserver
import thread

internetserver.init()
bluetoothserver.init()

try:
	thread.start_new_thread(internetserver.listen,())
	thread.start_new_thread(bluetoothserver.listen,())

except:
	print "Unable to create thread"

while 1:
	pass
