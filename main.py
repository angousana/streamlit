import ptp, time, os

def now():
    return int(time.time())
start=now()

while True:
    ptp.put("now.txt","Start: "+str(start)+"\nEnd: "+str(now()))