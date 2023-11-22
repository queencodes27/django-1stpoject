#  choyxonatech_app/routing.py

from django.urls import path
from . import consumers_module

websocket_urlpatterns = [
    path('choyxonatech_app/', consumers_module.ChatConsumer.as_asgi())
]

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
# ]

#room_name parametrini topadi URL ichidan va websocket connections handle qberadi