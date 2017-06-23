from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jenova.core.forms import LoginForm
# Create your views here.
def login(request):

    if request.method == 'POST':
        pass

    return render(request, 'login.html', {'form' : LoginForm()})

#@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard/index.html')

