import queue
import threading
import time

fifo_queue = queue.Queue()

lock = threading.RLock()


def hd(number):
    print(f"enter {number}")
    with lock:
        print(f"hi {number}")
        time.sleep(1)
        print(f"done {number}")
    print(f"exit {number}")


for n in range(3):
    cc = threading.Thread(target=hd, args=[n])
    fifo_queue.put(cc)
    cc.start()

"""
enter 0
hi 0
enter 1
enter 2
done 0
exit 0
hi 1
done 1
exit 1
hi 2
done 2
exit 2
"""
