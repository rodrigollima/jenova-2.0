from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class ClientView(View):
    def get(self, request):
        return HttpResponse('result')


# Create your views here.
def index(request):
    return render(request, 'list.html', {})