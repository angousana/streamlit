import ptp, time, os

def now():
    return int(time.time())
start=now()

while True:
    ptp.put("Start: "+str(start)+"\nEnd: "+str(now()))