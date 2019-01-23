import my_threading
import time

def printit():
  print "Hello, World!"
  print(5+10)
  my_threading.Timer(1.0, printit).start()


def timer():
    for _ in range(100):
        print(time.time())
        time.sleep(1)


import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something():
    print "Doing stuff..."
    # do your stuff
    s.enter(1, 1, do_something, ())

s.enter(0, 1, do_something, ())
s.run()