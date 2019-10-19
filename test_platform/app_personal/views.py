from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
# 用来写请求的处理逻辑
def hello(request):
    return render(request, "hello.html")


def login(request):
    """
    用户登录
    """
    # 返回登录页面
    if request.method == "GET":
        return render(request, "login.html")

    # 处理登录请求
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "login.html", {
                "error": "用户名或密码为空！"
            })

        user = auth.authenticate(username=username, password=password)
        print("用户是否存在？", user)
        if user is not None:
            auth.login(request, user)  # 记录用户的登录状态
            return HttpResponseRedirect("/mange/")
        else:
            return render(request, "login.html", {
                "error": "用户名或密码错误！"
            })


@login_required
def mange(request):
    """
    接口管理
    """
    return render(request, "manage.html")


def logout(request):
    """退出"""
    auth.logout(request)
    return HttpResponseRedirect("/")



# /form_action.asp?fname=admin&lname=admin123456
# /login_action/?username=admin&password=admin123456
# Http 请求：不记录状态的。





# django的处理过程：
# 1、url指定路径 /hello/
# 2、setting.py 找到url的配置文件。
# 3、urls.py匹配路径 /hello/ ，把请求指到 views 文件
# 4、再views.py 写 Response 的处理， 把 templates/ 目录下面的HTML文件，返回给客户端