from time import time, sleep

def pinger(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        print("execution time : {}".format(time() - t1))
    return wrapper


@pinger
def sleep_some(n):
    sleep(n)


sleep_some(3)    
