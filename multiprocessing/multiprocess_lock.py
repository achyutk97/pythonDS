import multiprocessing

def deposite(number, lock):
    for i in range(100):
        lock.acquire()
        number.value += 1
        lock.release()
    
def withdraw(number, lock):
    for i in range(10):
        lock.acquire()
        number.value -= 1
        lock.release()

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    amount = multiprocessing.Value("d", 1000.0)
    t1 = multiprocessing.Process(target=deposite, args=(amount, lock,))
    t2 = multiprocessing.Process(target=withdraw, args=(amount, lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(amount.value)