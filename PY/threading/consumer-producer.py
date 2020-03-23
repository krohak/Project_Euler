import threading
import queue
import random
import time

MAX_SIZE = 10
queue_sync = queue.Queue(MAX_SIZE)

class Producer(threading.Thread):
    def __init__(self, name=None):
        super(Producer, self).__init__()
        self.name = name
        

    def run(self):
        while True:
            if not queue_sync.full():
                item = random.randint(1,10)
                queue_sync.put(item)
                print('Putting ' + str(item)  + ' : ' + str(queue_sync.qsize()) + ' items in queue')
                time.sleep(random.randint(1,3))

class Consumer(threading.Thread):
    def __init__(self, name=None):
        super(Consumer, self).__init__()
        self.name = name
        

    def run(self):
        while True:
            if not queue_sync.empty():
                item = queue_sync.get()
                print('Getting ' + str(item)  + ' : ' + str(queue_sync.qsize()) + ' items in queue')
                time.sleep(random.randint(1,3))

Producer(name='Producer').start()
Consumer(name='Consumer').start()