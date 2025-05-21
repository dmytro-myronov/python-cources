from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
from typing import Tuple


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Обробник HTTP-запитів. Відповідає на GET-запити простим текстом."""

    def do_GET(self) -> None:
        """
        Обробляє GET-запит клієнта.
        Відправляє відповідь з текстовим повідомленням та поточним ім'ям потоку.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        response_text: str = (
            "Вітаю! Ви підключені до багатопотокового сервера.\n"
            f"Потік: {threading.current_thread().name}"
        )
        self.wfile.write(response_text.encode('utf-8'))


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """
    HTTP-сервер з підтримкою багатопоточності.
    Кожен запит обробляється в окремому потоці.
    """
    daemon_threads = True  # Автоматичне завершення потоків при завершенні сервера


def run_server(host: str = "localhost", port: int = 8000) -> None:
    """
    Запускає багатопотоковий HTTP-сервер.

    :param host: Хост, на якому запускається сервер (наприклад, 'localhost')
    :param port: Порт, на якому слухає сервер (наприклад, 8000)
    """
    server_address: Tuple[str, int] = (host, port)
    httpd = ThreadedHTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Сервер запущено на http://{host}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
