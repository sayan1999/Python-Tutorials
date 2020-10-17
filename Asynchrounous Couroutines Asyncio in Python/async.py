import asyncio, time, random

async def scarpe_url(url, Pass):
    fetch_time=random.randint(1, 5)
    await asyncio.sleep(fetch_time)
    print(f'Pass: {Pass}, Fetched url {url} in {fetch_time} seconds')
    return

async def main(urls, Pass=1):
    await sem.acquire()
    print(f'Pass {Pass} is entered')
    asyncio.ensure_future(main(urls, Pass+1))
    await asyncio.wait([scarpe_url(url, Pass) for url in urls])
    print(f'Pass: {Pass} is released')
    sem.release()


if __name__ == '__main__':
    
    max_coroutines = 10
    sem=asyncio.Semaphore(max_coroutines)
    urls=list(range(1, 10))
    eventloop=asyncio.get_event_loop()
    asyncio.ensure_future(main(urls))
    try:
        eventloop.run_forever()
    except KeyboardInterrupt:
        eventloop.close()