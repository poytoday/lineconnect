from django.shortcuts import render
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

YOUR_CHANNEL_ACCESS_TOKEN = "llll"

YOUR_CHANNEL_SECRET = "xxxx"

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