import concurrent.futures
import threading
import time
def do_something(seconds):
    print(f"Executing in for {seconds} seconds")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds}"

start=time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]#secs list
    # threads=[]
    #by using the for loop
    for i in range(5):
        f=executor.submit(do_something,secs[i])
        # threads.append(f)
# for f in threads:
#     print(f.result())
    # #by the help of List Comprehension and as_completed()
    # list1=[executor.submit(do_something,sec) for sec in secs]
    # for future in concurrent.futures.as_completed(list1):
    #     print(future.result())
    # #by the help if map() on the executor and getting the generator object
    # future_map_obj = executor.map(do_something, secs)
    # print(future_map_obj)
    # print(type(future_map_obj))
    # # for future in future_map_obj:
    # #     print(future)

#by the help of threading
# threads=[]
# secs=[5,4,3,2,1]
# for i in range(5):
#     t=threading.Thread(target=do_something,args=(secs[i],))
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
finish=time.perf_counter()
print(f"The Time Taken by the thread is {round(finish-start,2)}")
