from threading import Condition, Thread
import time
import random

numbers = []

def taskA(c):
    for _ in range(5):
        with c:
            num = random.randint(1, 10)
            print("Generated random number:", num)
            numbers.append(num)
            print("Notification issued")
            c.notify()
        time.sleep(0.3)

def taskB(c):
    for i in range(5):
        with c:
            print("waiting for update")
            while not numbers: 
                c.wait()
            print("Obtained random number", numbers.pop())
        time.sleep(0.3)

c = Condition()
t1 = Thread(target=taskB, args=(c,))
t2 = Thread(target=taskA, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")