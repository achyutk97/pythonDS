import threading
from time import sleep, time

number = [1, 2, 3, 4]

def cal_squre(number):
    print(number)
    for i in number:
        sleep(0.2)
        print("Squre of numbers", i * i)

def cal_cube(number):
    for i in number:
        sleep(0.2)
        print("Cube of numbers", i * i * i)
    
if __name__ == '__main__':
   
    t = time()
    t1 = threading.Thread(target=cal_squre, args=(number,))
    t2 = threading.Thread(target=cal_cube, args=(number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("time difference", time() - t)
