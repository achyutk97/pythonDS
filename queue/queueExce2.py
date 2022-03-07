from queue import Queue

class ExtraQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def front(self):
        return self.buffer[-1]

bin = ""
def decimalToBinary(decimal):
    global bin
    if decimal > 1:
        decimalToBinary(decimal//2)
    bin += str(decimal % 2)


def produce_binary_numbers(n):
    queue = ExtraQueue()
    queue.enqueue("1")

    for _ in range(n):
        front =  queue.front()
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")
        print(queue.dqueue())
        
if __name__ == "__main__":
    produce_binary_numbers(10)
