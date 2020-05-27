import aiohttp
import asyncio
from GetToken import tkn
import time

start_time = time.monotonic()

url = 'https://test-dh2.efir-net.ru/v2/Info/FintoolReferenceData'

token = tkn()

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}

async def fetch(session, url):
    async with session.post(url) as response:
        if response.status !=200:
            print('Error' + response.status)
        else:
            status = 'Ok'
    return status


async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        status = await fetch(session, url)
    return status

loop = asyncio.get_event_loop()
status = loop.run_until_complete(main())

ET = time.monotonic() - start_time

print(status + " {:>.2f}".format(ET))
