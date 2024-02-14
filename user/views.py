from django.http import request
from .models import User
from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest

# noinspection PyBroadException
from django.http import HttpResponse
'''
判断两次密码输入是否一致的语句中，你使用了try...except，但在此情况下，两次密码的比较操作不会引发任何异常，因此这里的用法不正确。

在Django处理HTTP请求的视图函数中，返回结果应当是一个HttpResponse对象或者继承自HttpResponse的对象，比如render
函数返回的结果。所以，你需要将消息用HttpResponse函数包装起来再返回。


'''


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
        # GET 返回提交数据
    elif request.method == 'POST':
        recent_username = request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # POST 处理提交数据
        #   1. 两个密码都要保持一致
        if password_2 != password_1:
            return HttpResponse("Two time passwords are not same")

        #   2. 当前用户名是否可用
        old_name = User.objects.filter(username=recent_username)
        if old_name:
            return HttpResponse("This account is already register")
        #   3. 插入数据
        else:
            User.objects.create(username=recent_username, password=password_1)
            return HttpResponse('Success')
