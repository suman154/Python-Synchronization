from threading import Condition, Thread
import time

c = Condition()

def thread_a():
    print("Thread A started")
    with c:
        print("Thread A waiting for permission...")
        c.wait()
        print("Thread A got permission!")
    print("Thread A finished")

def thread_b():
    print("Thread B started")
    with c:
        time.sleep(2)
        print("Notifying Thread A...")
        c.notify()
    print("Thread B finished")

Thread(target=thread_a).start()
Thread(target=thread_b).start()