import multiprocessing
from time import sleep, time
import multithreading_task as mt

if __name__ == '__main__':
    t = time()

    t1 = multiprocessing.Process(target=mt.cal_cube, args=(mt.number,))
    t2 = multiprocessing.Process(target=mt.cal_squre, args=(mt.number,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("time differneces", time() - t)