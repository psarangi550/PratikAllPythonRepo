import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)
    print("Pratik")

loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()