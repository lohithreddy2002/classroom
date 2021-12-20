# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from api.models import Contact

from api.models import Message
from api.models import Chat
from api.serializers import MessageSerializer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def send_message(self,data):
        chat = Chat.objects.get(id = data["chat_id"])
        contact = Contact.objects.get(user = self.scope['user'])
        message = Message.objects.create(user = contact,content = data["message"])
        chat.messages.add(message)
        chat.save()
        content = {
            'command': 'message',
            'message': MessageSerializer(message).data
        }
        return self.send_chat_message(content)
    
    def fetch(self,data):
        print("fetch")



    functions = {
        "send_message":send_message,
        "fetch":fetch
    }

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.functions[text_data_json['command']](self,text_data_json)

    # Receive message from room group
    def send_chat_message(self, event):
        message = event['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self,event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps(message))