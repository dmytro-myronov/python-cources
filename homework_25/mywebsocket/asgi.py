import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import company.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mywebsocket.settings")
django.setup()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            company.routing.websocket_urlpatterns
        )
    ),
})
