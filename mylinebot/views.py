from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from linebot import (LineBotApi, WebhookHandler)
# Create your views here.


from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage,
    ImageSendMessage,
)

import os

YOUR_CHANNEL_ACCESS_TOKEN = "Jj5eUbAaxbih/MD5lRO14aSZuf/OaGwUso3MGMFdaYp1GzhYJ6YY0SjTtORth34U8WJKq6FJCrZd1TxOwLPHEs2VWKONd6ChoEeaIdeOWt0FTsUZy5NTU6dKdK4gfPQ28EmANDrZqO/uMX8uT1wmkwdB04t89/1O/w1cDnyilFU="

YOUR_CHANNEL_SECRET = "ed6549ba0d323dcb0f2b55d2864fc22f"

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    print('Here is callback function')
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    print(body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=200)



@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    # print('Here is handle_text_message function')
    dict_event = event.__dict__
    # print(dict_event)		

   	line_bot_api.reply_message(event.reply_token, TextSendMessage(text='สวัสดี'))