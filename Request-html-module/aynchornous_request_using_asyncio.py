import asyncio#importing the asyncio module for working with coroutin
import time #importing the time module
from requests_html import AsyncHTMLSession
async_html=AsyncHTMLSession()
t1=time.perf_counter()
async def task1():
    resp=await async_html.get("https://httpbin.org/delay/3")
    return resp
async def task2():
    resp=await async_html.get("https://httpbin.org/delay/6")
    return resp
async def task3():
    resp=await async_html.get("https://httpbin.org/delay/9")
    return resp
async def task4():
    resp=await async_html.get("https://httpbin.org/delay/12")
    return resp
responses=async_html.run(task1,task2,task3,task4)
for resp in responses:
    print(resp.url)
t2=time.perf_counter()
print(t2-t1)