from django.views import View
from django.http import HttpResponse

class ClientApiView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('result api')
