import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing
import alarms.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket.settings")

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(
            #chat.routing.websocket_urlpatterns,
            alarms.routing.websocket_urlpatterns,
        )
    ),
})