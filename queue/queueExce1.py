from queue import Queue
import threading
import time

orders = ['pizza','samosa','pasta','biryani','burger']
class Orders(Queue):
    def __init__(self) -> None:
        super().__init__()

    def equeue(self, *data):
        for i in data:
            print(i, "Order is placed")
            super().enqueue(i)
            time.sleep(0.5)
    
    def dequeue(self):
        time.sleep(1)
        while self.size() > 0:
            data = super().dqueue()
            print(data, "Order is server")
            time.sleep(2)
        else:
            print("All order completed")

data = Orders()

t1 = threading.Thread(target=data.equeue, args=orders)
t2 = threading.Thread(target=data.dequeue)

t1.start()
t2.start()

t1.join()
t2.join()