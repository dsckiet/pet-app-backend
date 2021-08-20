import asyncio
import json
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Message

class ChatConsumer(AsyncConsumer ):
    def __init__(self):
        self.sender = ""
        self.receiver = ""
    async def websocket_connect(self , event):
        print("connected" , event)
        await self.send(
            {
                "type":"websocket.accept"
            }
            )
        await self.send({
            "type":"websocket.send",
            "text":"heya!!"
        })
        self.receiver = self.scope['url_route']['kwargs']['username']
        self.sender = self.scope['user']
        print(self.receiver , self.sender)

    async def websocket_receive(self , event ):
        print(event)
        msg_obj = await self.chat(event['text'] ,self.sender , self.receiver)
        # event == {'type': 'websocket.receive', 'text': 'sadsa'}
        print("received" , event)

    async def websocket_disconnect(self , event):
        print("disconnected" , event)

    @database_sync_to_async
    def chat(self , msg , sender , receiver):
        receiver = User.objects.get(username = receiver)
        sender = User.objects.get(username = sender)
        new_msg =  Message.objects.create(
            author_id = sender.id,
            receiver_id = receiver.id,
            message = msg
        )
        print("msgs created")
        return new_msg

