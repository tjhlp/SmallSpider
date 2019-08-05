import time
def count_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('处理数据用时:{}'.format(end_time - start_time))
        return result

    return inner