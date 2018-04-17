from django.shortcuts import render,HttpResponse
from .models import Role
from django.utils.safestring import mark_safe
import json




def index(request):
    return render(request,'chat/index.html',{})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def query(request):
    res = Role.objects.all()
    print(res)
    return HttpResponse('....')
