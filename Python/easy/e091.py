# 26/11/2019
import asyncio
import sys
import threading


async def sleep(x):
    await asyncio.sleep(x)
    print(x)
    return None


async def sleep_sort(numbers):
    await asyncio.gather(*(sleep(x) for x in numbers))
    return None


if sys.argv[1] in ["-a", "--async"]:  # async/await coroutines
    n = [int(x) for x in sys.argv[2:]]
    asyncio.run(sleep_sort(n))

else:  # multithreading
    for x in sys.argv[1:]:
        threading.Timer(int(x), print, args=[x]).start()
