import os
from datetime import timedelta, datetime

start = datetime.now()

x = 1
while x < 1000000000:
    x += 1
    print(x)

    from_start = datetime.now() - start
    print(from_start.seconds)
    my_pid = os.getpid()
    if from_start.seconds >= 2:
        os.kill(my_pid, 15)