# whole timing mechanism has been encapsulated into
# a function so we don't repeat code. 

from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

def measure(func):
    t = time()
    func()

print(func.__name__, 'took:', time() - t)