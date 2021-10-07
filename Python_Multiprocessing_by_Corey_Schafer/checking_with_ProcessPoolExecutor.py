import concurrent.futures
import time
start=time.perf_counter()
def do_something(seconds):#seconds is the args to the do_something_function
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping for {seconds} time"
seconds_time=[5,4,3,2,1]
with concurrent.futures.ProcessPoolExecutor() as executor:
    results=[executor.submit(do_something,sec) for sec in seconds_time]
    # results=executor.map(do_something,seconds_time)
    for result in results:
        # print(result)
        print(result.result())
finish=time.perf_counter()
print(f"Time Difference {round(finish-start,2)}")

