from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt 
# from webApp.models import Token,User
# from webApp.models import User,Token,Expence
from .models import * #Expence,Income,Token,User
from django.contrib.auth.models import User
import datetime
# Create your views here.
@csrf_exempt
def submit_expence(request):
    # print("'we are here'")
    # print(request.POST)
    now=datetime.datetime.now()
    this_token=request.POST['token']
    expence_text=request.POST['text']
    expence_amount=request.POST['amount']
    this_user=User.objects.filter(token__token=this_token).get()
    print(expence_text)
    print(expence_amount)
    print(this_user)
    print(now)
    # Expence.objects.Create(text=expence_text,amount=expence_amount,date=now,user=this_user)
    Expence.objects.create(text=expence_text,amount=expence_amount,date=now,user=this_user)
    
    return JsonResponse({'status':'ok',},encoder=json.JSONEncoder)
    
