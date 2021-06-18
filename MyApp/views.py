from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MyApp.models import *

@login_required
def welcome(request):
    print('我进来了')
    return render(request, 'welcome.html')

#返回子页面
def child(request, eid, oid):

    res = child_json(eid)

    return render(request, eid, res)

#进入主页
@login_required
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "Home.html", "oid": ""})

def login(request):
    return render(request, 'login.html')

#开始登录
def login_action(request):
    u_name =  request.GET['username']
    p_word = request.GET['password']

    # 开始 链接 django 用户库，查看用户名密码是否正确
    user = auth.authenticate(username=u_name, password=p_word)
    # 返回前端告诉前端账号密码对不对
    if user is not None:
        #return HttpResponseRedirect('/home/')
        auth.login(request, user)
        request.session['user'] = u_name
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

#注册
def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']

    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse('注册成功')
    except:
        return HttpResponse('注册失败~用户名被占用~~')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

# 吐槽函数
def pei(request):
    tucao_text = request.GET['tucao_text']

    DB_tucao.objects.create(user=request.user.username, text=tucao_text)

    return HttpResponse('')

# 帮助
def api_help(request):
    return render(request, 'welcome.html', {"whichHTML": "help.html", "oid": ""})

# 控制不同的页面返回不同的数据：数据分发器
def child_json(eid):
    res = {}
    if eid == 'Home.html':
        date = DB_home_href.objects.all()
        res = {"hrefs": date}
    if eid == 'project_list.html':
        date = DB_project.objects.all()
        res = {"projects": date}

    return res

# 进入项目列表
def project_list(request):
    return render(request, 'welcome.html', {"whichHTML": "project_list.html", "oid": ""})

# 删除项目
def delete_project(request):
    id = request.GET['id']

    DB_project.objects.filter(id=id).delete()

    return HttpResponse('')