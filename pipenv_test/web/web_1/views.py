# from django.shortcuts import render
from django.http import HttpResponse
from web_1.models import Test_1
import json
# Create your views here.


def index(request):
    #print(Test_1.objects.values_list())
    jf = list(Test_1.objects.values_list())
    return HttpResponse(jf)

