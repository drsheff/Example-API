import aiohttp
import asyncio

headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
}

url = ''
login = ''
passwd = ''

def tkn():

    async def fetch(session, url):
        params = {'login': login, 'password': passwd}
        async with session.post(url, json=params) as response:
            resp = await response.json()
            token = resp['token']
            return token

    async def main():
        async with aiohttp.ClientSession(headers=headers) as session:
            t = await fetch(session, url)
        return t

    loop = asyncio.get_event_loop()
    tk = loop.run_until_complete(main())

    return tk

tkn()
