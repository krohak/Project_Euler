from threading import Thread, Condition
import random
from time import sleep

MAX_SIZE = 3
queue = []

lock = Condition()

class Producer(Thread):
    def run(self):
        while True:
            with lock:
                if len(queue) == MAX_SIZE:
                    print("Producer waiting since max size reached")
                    lock.wait()
                item = random.randint(1,10)
                queue.append(item)
                print("Adding {} to queue".format(item), len(queue))
                lock.notify()
            sleep(random.randint(1,10) if random.randint(0,1) else random.random())
        

class Consumer(Thread):
    def run(self):
        while True:
            with lock:
                if not queue:
                    print("Consumer waiting since 0 size reached")
                    lock.wait()
                item = queue.pop(0)
                print("Removed {} from queue".format(item), len(queue))
                lock.notify()
            sleep(random.randint(1,10) if random.randint(0,1) else random.random())


Producer().start()
Consumer().start()

