from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

def welcome(request):
    print('我进来了')
    return render(request, 'welcome.html')

#返回子页面
def child(request, eid, oid):
    return render(request, eid)

def home(request):
    return render(request,'welcome.html',{"whichHTML": "Home.html","oid": ""})

def login(request):
    return render(request, 'login.html')

#开始登录
def login_action(request):
    u_name =  request.GET['username']
    p_word = request.GET['password']

    #开始 链接 django 用户库，查看用户名密码是否正确
    user = auth.authenticate(username=u_name, password=p_word)
    if user is not None:
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponse('')

#注册
def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']

    user = auth.authenticate(username=u_name)
    if user is None:

    else:
        return HttpResponse('')