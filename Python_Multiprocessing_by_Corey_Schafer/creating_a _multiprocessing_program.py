#here we have to use the multi processing module instead of threading module
import multiprocessing#importing the multiprocessing module
import time #importing the time module
start=time.perf_counter()#using the perf_conter function to evaluate time
def do_something(seconds):#seconds is the args to the do_something_function
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds} time"


results=[]#empty list object
for _ in range(10):#using the for loop with throw away variable
    p1=multiprocessing.Process(target=do_something,args=[1.5])
    p1.start()#staring the processed
    results.append(p1)

#now using the join method so that the main thread will not be completed
for result in results:
    result.join()

finish=time.perf_counter()
print(f"The time difference is {round(finish-start,2)}")


