# choyxonatech_app/consumers_module.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer # it is base class for building asynch Websocket connections in Django Channels

class ChatConsumer(AsyncWebsocketConsumer): #this class ll handle WebS connections for my app
    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            'type': 'websocket.accepted'
        })


        # self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        # await self.channel_layer.group_add(
            # self.room_group_name,
            # self.channel_name
        # )

        # await self.accept()

    async def websocket_disconnect(self, event):
        print('disconnected', event)

        # Leave room group
        # await self.channel_layer.group_discard(
            # self.room_group_name,
            # self.channel_name
        # )

    async def websocket_receive(self, event):
        print('received', event)


        # text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        # Send message to room group
        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
                # 'type': 'chat.message',
                # 'message': message
            # }
        # )
    #
    # async def chat_message(self, event):
    #     message = event['message']
    #
        # Send message to WebSocket
        # await self.send(text_data=json.dumps({
        #     'message': message
        # }))
