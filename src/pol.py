import time
import threadpool


def sayhello(str):
    print("Hello {}".format(str))


name_list = ['xiaozi', 'aa', 'bb', 'cc']
start_time = time.time()
pool = threadpool.ThreadPool(2)
requests = threadpool.makeRequests(sayhello, name_list)
[pool.putRequest(req) for req in requests]
pool.wait()
