import multiprocessing
import os

def function(queue):
    print("parent pid", os.getppid())
    queue.put(f"hellow from {os.getpid()}")

if __name__ == "__main__":
    qu =  multiprocessing.Queue(maxsize=2)
    p1 = multiprocessing.Process(target=function, args=(qu,), name="process1")
    p2 = multiprocessing.Process(target=function, args=(qu,), name="process1")

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(qu.get())
    print(qu.get())

