#made by Sathwik R - www.github.com/cicada0007

#1/usr/bin/python3



import threading


def loop1():
    while True:
        print("loop1")

def loop2():
    while True:
        print("loop2")

t1 = threading.Thread(target=loop1)
t1.start()
loop2()        
