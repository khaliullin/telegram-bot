import json

from bot_extra.settings import URL
import requests


def send_message(chat_id, text):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    print(r.json())


def get_chat_id(request):
    r = json.loads(request.body)
    chat_id = r['message']['chat']['id']
    return chat_id


def get_text(request):
    r = json.loads(request.body)
    text = r['message']['text']
    return text