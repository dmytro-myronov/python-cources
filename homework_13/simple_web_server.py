import asyncio
from aiohttp import web


async def handle(request):
    return web.Response(text="Hello, World!")

async def get_slow(request):
    await asyncio.sleep(15)
    return web.Response(text=f"Hello, slow method!")

async def get_news(request):
    return web.Response(text="News will be here!")


app = web.Application()


app.router.add_get('/', handle)
app.router.add_get('/slow', get_slow)
app.router.add_get('/news', get_news)

PORT = 8000


if __name__ == '__main__':
    web.run_app(app, port=PORT)
