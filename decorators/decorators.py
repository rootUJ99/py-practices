import time

def log_time_complete(fn):
    def inner(*args, **kwrgs):
        start_time = time.time()
        res = fn(*args, **kwrgs) 
        end_time = time.time()
        print("time taken", end_time - start_time)
        return res
    return inner

def some_compute_sum(loop_till: int):
    sum = 0
    for i in range(loop_till):
        sum += i
    return sum

@log_time_complete
def some_compute_mul(loop_till: int):
    mul = 1
    for i in range(loop_till):
        if i == 0:
            continue
        mul *= i
    return mul 


if __name__ == "__main__":
    computed_sum = log_time_complete(some_compute_sum)
    sum_res = computed_sum(10000)
    print(sum_res)

    mul_res = some_compute_mul(999)
    print(mul_res)
