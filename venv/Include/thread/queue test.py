from multiprocessing import Process, Queue
import time, random, os


def consumer(q):
    while True:
        time.sleep(random.randint(1, 3))
        res = q.get()
        if res is None: break
        print('\033[45m消费者拿到了：%s\033[0m' % res)


def producer(seq, q):
    for item in seq:
        time.sleep(random.randint(1, 3))
        print('\033[46m生产者生产了：%s\033[0m' % item)

        q.put(item)


if __name__ == '__main__':
    q = Queue()

    c = Process(target=consumer, args=(q,))
    c.start()

    producer(('包子%s' % i for i in range(5)), q)
    q.put(None)
    c.join()
    print('主线程')