import time #importing the time module
from requests_html import HTMLSession
html=HTMLSession()
t1=time.perf_counter()
resp1=html.get("https://httpbin.org/delay/3")
print(resp1.url)
resp1=html.get("https://httpbin.org/delay/6")
print(resp1.url)
resp1=html.get("https://httpbin.org/delay/9")
print(resp1.url)
resp1=html.get("https://httpbin.org/delay/12")
print(resp1.url)
t2=time.perf_counter()
print(t2-t1)