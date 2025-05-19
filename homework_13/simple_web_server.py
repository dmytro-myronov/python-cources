import asyncio
from aiohttp import web
from typing import Awaitable


async def handle(request: web.Request) -> web.Response:
    """
    Обработчик для главной страницы.

    Args:
        request (web.Request): Входящий HTTP-запрос.

    Returns:
        web.Response: HTTP-ответ с текстом "Hello, World!".
    """
    return web.Response(text="Hello, World!")


async def get_slow(request: web.Request) -> web.Response:
    """
    Обработчик, имитирующий медленную операцию.

    Args:
        request (web.Request): Входящий HTTP-запрос.

    Returns:
        web.Response: HTTP-ответ с текстом "Hello, slow method!" через 15 секунд.
    """
    await asyncio.sleep(15)
    return web.Response(text="Hello, slow method!")


async def get_news(request: web.Request) -> web.Response:
    """
    Обработчик для страницы новостей.

    Args:
        request (web.Request): Входящий HTTP-запрос.

    Returns:
        web.Response: HTTP-ответ с текстом "News will be here!".
    """
    return web.Response(text="News will be here!")


app: web.Application = web.Application()

app.router.add_get('/', handle)
app.router.add_get('/slow', get_slow)
app.router.add_get('/news', get_news)

PORT: int = 8000


if __name__ == '__main__':
    web.run_app(app, port=PORT)
