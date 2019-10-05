from django.shortcuts import render
#导入Http对象
from django.http import HttpResponse
#创建index视图
#每个视图中至少有一个httpResponsse对象，定义在django.http中
#每个视图至少返回一个HttpResponse对象
def index(request):
    return HttpResponse("Login action here!")
