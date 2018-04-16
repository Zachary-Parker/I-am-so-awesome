from django.shortcuts import render,HttpResponse
from .models import Role
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    if user == 'Parker' and pwd == '123':
        return HttpResponse('Welcome!')
    return HttpResponse('Login Failed')

def query(request):
    res = Role.objects.all()
    print(res)
    return HttpResponse('....')



def fix():
    return 'fixation'