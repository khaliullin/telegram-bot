from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot_extra.functions import *


@csrf_exempt
def index(request):
    if request.method == "GET":
        return HttpResponse('It works!!!!')
    else:
        chat_id = get_chat_id(request)
        text = get_text(request)

        send_message(chat_id, text)

        return HttpResponse('Post works!')

