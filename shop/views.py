from django.http import HttpResponse
from django.views import View


class Index(View):
    def get(self, request):
        return HttpResponse('It works!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Post works!')
