import asyncio  # 异步协程
import aiohttp

urls = [
    "https://i1.huishahe.com/uploads/allimg/202205/9999/a703018f22.jpg",
    "https://i1.huishahe.com/uploads/allimg/202206/9999/9783c7e78d.jpg",
    "https://i1.huishahe.com/uploads/allimg/202205/9999/cce11863bd.jpg"
]


async def aiodownload(url):
    name = url.split("/", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    print("ok")
