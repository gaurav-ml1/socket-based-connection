from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from .socket_authentication import EquipmentAuthenticationMiddleware
from .server_socket import SocketConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': EquipmentAuthenticationMiddleware(
        URLRouter([
        url(r"^api/channels/device/$", SocketConsumer),
    ])
    ),
})
