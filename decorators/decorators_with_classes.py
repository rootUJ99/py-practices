from time import time


class DecoratorsWithClass:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args, **kwrgs):
        start_time = time()
        res = self.func(*args, **kwrgs)
        end_time = time()
        print("print time taken",end_time - start_time)
        return res

@DecoratorsWithClass
def compute_sum(loop_range):
    sum = 0
    for i in range(loop_range):
        sum += i
    return sum 

if __name__ == "__main__":
    sum = compute_sum(10000)
    print(sum)
