from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)

    def dqueue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def printQueue(self):
        print(self.buffer)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue({"q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            }})
    queue.enqueue({"q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }})

    queue.printQueue()
    print(queue.dqueue())
    queue.printQueue()
    print(queue.size())
    print(queue.isEmpty())