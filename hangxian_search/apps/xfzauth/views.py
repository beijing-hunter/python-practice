from io import BytesIO  # 用来存储这些字节流

from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # 导入messages模块进行错误消息的传递
from django.http import HttpResponse

from utils.aliyunsdk import aliyun
from utils.captcha.hycaptcha import Captcha
from .forms import LoginFrom, RegisterForm  # 导入form表单
# authentivate 用来验证用户是否登录，login和logout的登录和登出
from .models import User
from .models import findUserByPhone
# from django.forms.utils import ErrorDict
from utils import restful


# 两种写法
# 1.定义函数法
# def login_view(request):
# 	if request.method == 'GET':
# 		return render(request,'auth/login.html')


class LoginView(View):
    """
    登录
    2使用类写法
    """

    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        form = LoginFrom(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get("telephone")
            password = form.cleaned_data.get("password")
            remember = form.cleaned_data.get("remember")
            # authenticate函数是判断凭证是否有效，有效返回一个user对象
            user = findUserByPhone(telephone)
            olePassword = user.password
            pwdSuccess = False

            if not user.password is None:
                pwdSuccess = user.check_password(password)

            if user and pwdSuccess:
                # 登陆成功
                request.session["userId"] = user.id
                request.session["userName"] = user.username
                if remember:
                    # 如果设置过期时间位None,那么就会使用默认的过期时间
                    # 默认的过期时间位2个星期，14天
                    print("session默认时长14天")
                    request.session.set_expiry(None)
                else:
                    # 如果设置过期时间位0，那么浏览器关闭时就会结束
                    print("session时长为关闭浏览器时结束")
                    request.session.set_expiry(0)
                # 如果登陆成功，就返回首页
                print("验证登录成功！")
                return redirect(reverse('ticket:search'))
            else:
                # print("用户名或密码错误！", '电话 ：%s' % telephone, '密码 ：%s' % password)
                messages.info(request, "用户名或密码错误！")
                # message中包含由3中消息，1.info：提示消息；2.error：错误消息；3.debug：调试消息
                return redirect(reverse('xfzauth:login'))
        else:
            # print("表单验证失败！")
            messages.info(request, "表单验证失败！")
            return redirect(reverse('xfzauth:login'))



class RegisterView(View):
    """注册"""

    def get(self, request):
        return render(request, "auth/register.html")

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid() and form.validate_data(request):
            telephone = form.cleaned_data.get('telephone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(
                telephone=telephone, username=username, password=password)
            print('电话：%s' % telephone, '密码：%s' % password)
            request.session["userId"] = user.id  # 注册成功后，直接跳转到登录状态
            request.session["userName"] = user.username
            return restful.ok()
        else:
            message = form.get_error()
            return restful.params_error(message=message)


def logout_view(request):
    """退出登录"""
    del request.session["userId"]
    del request.session["userName"]
    return redirect(reverse('xfzauth:login'))


