from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
import random
from math import cos
from django.views.decorators.csrf import csrf_exempt,csrf_protect 

import json
from django.db.models import Q
from .models import Article, Comment, Users, Content
from .forms import CommentForm




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return ip



def index(request):    

    return render(request, 'index.html')


def generate_trajectory (x, y):
    axis = random.randint(10,170)
    start = random.randint(0, x)
    position = [start]
    for i in range(1, y):
        if position[i-1] == 0 or position[i-1] == x:
            axis = 180-axis
            position_new = position[i-2]
        else:
            position_new = (position[i-1] + 1/cos(axis* 0.01745329252))
        if position_new <0:
            position_new=0
        elif position_new>x:
            position_new = x

        position.append(position_new)

    return position

@csrf_exempt
def set_content(request):
    
    if request.method == "POST":

        max_width = int(request.POST.get('width'))
        max_height = int(request.POST.get('height'))
        print("h: ", max_height, " w: ", max_width)

        arr = generate_trajectory(max_width, max_height)
        

    return JsonResponse({
        'list': arr,
        'operation_status': 'ok'
    })


# Выводим страницу с контактами
def contacts(request):
    return render(request, 'contacts.html')
