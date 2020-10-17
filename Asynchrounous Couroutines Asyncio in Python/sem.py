import asyncio

sem=asyncio.Semaphore(1)

async def countdown():
    
    await sem.acquire() # 0
    print('start countdown')
    for i in range(4):
        await sem.acquire() # 0
        print(4-i-1)
    print('executed final')

async def do_something():
    for i in range(4):
        await asyncio.sleep(1)
        sem.release() # 1
        
    
if __name__ == '__main__':
    
    loop=asyncio.get_event_loop()
    asyncio.ensure_future(countdown())
    asyncio.ensure_future(do_something())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()