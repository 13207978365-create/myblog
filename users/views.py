from django.shortcuts import render

from users.forms import RegisterForm
from users.models import UserProfile
from utils.send_verify_code import send_verify_email


def user_register(request):
    '''
    用户的注册
    1. 用户想要注册, 则直接进入到此页面
    2. 用户点击注册来注册账号可以根据不同的请求方法来做不同的请求事件
    '''
    if request.method == 'GET':
        # 如果是get请求则直接进入到注册页面
        return render(request, 'user_register.html')
    else:
        # 如果是post请求, 则代表是点击了注册进行提交数据
        register_form = RegisterForm(request.POST)  # 生成表单进行验证
        if register_form.is_valid():  # 调用forms表单的方法来校验
            # 如果校验正确, 获取前端提交的数据
            email = register_form.cleaned_data.get('email')
            pwd = register_form.cleaned_data.get('password')
            nick_name = register_form.cleaned_data.get('nick_name')
            # 在用户类当中查询当前用户是否存在, 因为将email保存到username字段, 所以通过这样来查询数据
            user = UserProfile.objects.filter(username=email)
            # 如果能够查询到数据, 就代表该邮箱已经注册, 查询不到代表该邮箱还没注册
            if user:
                # 如果用户存在, 则回到注册页面, 同时给于一定的提示, 该字符串通过模板语言传递到模板当中去
                return render(request, 'user_register.html', {'msg': '用户名已存在'})
            else:
                # 如果用户不存在则保存信息
                user = UserProfile()
                user.username = email
                user.email = email
                user.nick_name = nick_name
                user.set_password(pwd)  # 将密码加密后保存
                user.save()
                # 发送邮件
                send_verify_email(email)
                return render(request, 'wait_start.html')

        else:
            # 如果校验错误, 就代表我们提交的数据不符合表单的要求, 则回到注册页面, 然后通过表单将错误信息展示到页面上
            return render(request, 'user_register.html', {'register_form':register_form})