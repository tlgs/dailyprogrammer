# 26/11/2019
import argparse
import asyncio
import multiprocessing
import sys
import threading
import time


def sleep_print(x):
    time.sleep(x)
    print(x)
    return None


async def asleep_print(x):
    await asyncio.sleep(x)
    print(x)
    return None


async def sleep_sort(numbers):
    await asyncio.gather(*(asleep_print(x) for x in numbers))
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--coroutines", action="store_true")
    group.add_argument("-t", "--threads", action="store_true")
    group.add_argument("-p", "--processes", action="store_true")
    args = parser.parse_args()

    numbers = []
    for line in args.file:
        x = int(line.strip())
        numbers.append(x)

    if args.threads:
        for x in numbers:
            threading.Timer(x, print, args=[x]).start()

    elif args.processes:
        for x in numbers:
            multiprocessing.Process(target=sleep_print, args=[x]).start()

    else:
        asyncio.run(sleep_sort(numbers))
