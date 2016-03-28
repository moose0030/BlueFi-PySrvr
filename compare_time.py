import time
from datetime import datetime

def isTimeLaterThanNow(timeString):
    t = time.strptime(timeString, "%H:%M:%S")
    now = datetime.now().time()
    other = datetime.now().time()
    other = other.replace(hour = t.tm_hour, minute = t.tm_min, second = t.tm_sec)
    print other
    print now
    return other >= now

def testTLTT():
    time1 = "16:03:00"
    time2 = "01:34:59"
    time3 = "21:33:59"
    
    print isTimeLaterThanNow(time1)
    print isTimeLaterThanNow(time2)
    print isTimeLaterThanNow(time3)
    

