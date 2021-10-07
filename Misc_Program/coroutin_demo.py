import asyncio#importing the asyncio module
import time #importing the time module
async def print_dur():
    start_time=time.time()
    while True:
        dur_time=int(time.time()-start_time)
        if dur_time%3==0:
            print(f"The duration is {dur_time} seconds")
        await asyncio.sleep(1)
async def print_num():
    num=1
    while True:
        print(num)
        num+=1
        await asyncio.sleep(0.3)
async def main():
    task1=asyncio.create_task(print_dur())
    task2=asyncio.create_task(print_num())
    await asyncio.gather(task1,task2)

loop=asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()