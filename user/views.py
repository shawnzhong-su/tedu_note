import hashlib

from django.http import request
from hashlib import md5
from .models import User
from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponseRedirect
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
        # Hash - Password
        '''
        m.update(password_1.encode()) 这段代码中的 encode() 方法是将字符串（在 Python 中字符串是 
        Unicode）转换为字节串，也就是 bytes 类型。
        这在 Python 3 以后的版本中是必要的，因此字节串（bytes）类型与字符串（str）类型被明确区分。
        str类型是用于存储文本数据，或者说是Unicode字符序列。
        bytes类型是用于存储二进制数据，或者说是字节序列。

        '''
        m = hashlib.md5()
        m.update(password_1.encode())
        hashpassword = m.hexdigest()
        #   2. 当前用户名是否可用
        old_name = User.objects.filter(username=recent_username)
        if old_name:
            return HttpResponse("This account is already register")
        #   3. 插入数据
        try:
            user = User.objects.create(username=recent_username,
                                       password=hashpassword)
            # 有可能 报错-重复插入［唯一索引注意并发写入问题］
        except Exception as e:
            print(
                'create users error %s' % e
            )
            return HttpResponse('This account is already register.')
        # 免注册
        request.session['username'] = recent_username
        request.session['uid'] = user.id
        # TODO 修改session 存储时间为 1 天
        return HttpResponseRedirect('/index')


def login_view(request):
    if request.session.get('username') and request.session.get('uid'):
        return HttpResponseRedirect('/index')
    cookies_username = request.COOKIES.get("username")
    cookies_uid = request.COOKIES.get("uid")
    if cookies_username and cookies_uid:
        request.session['username'] = cookies_username
        request.session['uid'] = cookies_uid
        return HttpResponseRedirect('/index')

    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method == "POST":
        cur_username = request.POST['username']
        cur_password = request.POST['password']
        try:
            user = User.objects.get(username=cur_username)
        except Exception as e:
            print('-- login user error %s' % e)
            return HttpResponse('Your Username or Account is Wrong')
        m = hashlib.md5()
        m.update(cur_password.encode())
        if m.hexdigest() != user.password:
            return HttpResponse('Your Username or Account is Wrong')

        request.session['username'] = cur_username
        request.session['uid'] = user.id

        resp = HttpResponseRedirect('/index')
        if 'remember' in request.POST:
            resp.set_cookie('username', cur_username, 3600 * 24 * 3)
            resp.set_cookie('uid', user.id, 3600 * 24 * 3)
        return resp


def logout_view(request):
    if 'username' in request.session:
        del request.session['username']
    if 'uid' in request.session:
        del request.session['uid']

    response = HttpResponseRedirect('/index')
    if 'uid' in request.COOKIES:
        response.delete_cookie('uid')
    if 'username' in request.COOKIES:
        response.delete_cookie('username')
    return response
