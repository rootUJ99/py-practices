import time
def gen():
    for i in range(10):
        time.sleep(1)
        yield i

def with_for_loop():
    for i in gen():
        print(i)

def with_next():
    try:
        genr = gen()
        while(True):
            print(next(genr))
    except(StopIteration):
        return

def main():
    with_for_loop()
    with_next()
if __name__ == "__main__":
    main()
