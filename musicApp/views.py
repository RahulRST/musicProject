from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        if(username == 'admin' and password == 'admin'):
            return redirect('/home')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')