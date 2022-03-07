import multiprocessing

# Sharing the variables between two process
def cal_cube(number, arra, v, q):
    v.value = 100
    for i, value in enumerate(number):
        arra[i] = value * value * value
        q.put(value*value)


if __name__ == '__main__':
    arra = multiprocessing.Array("i", 4)
    v = multiprocessing.Value("d", 0)
    queue = multiprocessing.Queue()
    number = [1, 2, 3, 4]
    t1 = multiprocessing.Process(target=cal_cube, args=(number, arra, v, queue,))
    t1.start()
    t1.join()
    print(arra[:])
    print(v.value)
    while queue.empty() is False:
        print(queue.get())