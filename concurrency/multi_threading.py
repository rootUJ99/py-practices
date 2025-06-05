import threading
import os
def func1():
    print(f"from pid {os.getpid()}")
    print(f"from thread {threading.current_thread().name}")
    print("hello form func 1")

def func2():
    print(f"from pid {os.getpid()}")
    print(f"from thread {threading.current_thread().name}")
    print("hello form func 2")
 

if __name__ == "__main__":
    t1 = threading.Thread(target=func1, args=(), name="thread1")
    t2 = threading.Thread(target=func2, args=(), name="thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()


