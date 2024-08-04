import time


class Iterator:
    def __init__(self, list):
        self.list = list 
        self.curr = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.curr += 1
            time.sleep(1)
            return self.list[self.curr]
        except(IndexError):
            raise StopIteration


def main():
    it = Iterator([10, 20, 550, 66])
    for i in it:
        print(i)

if __name__ == "__main__":
    main()
