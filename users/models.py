from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
class UserProfile(AbstractUser):
    """
    用户表
    1. username(Django提供字段): 用户名, 唯一. 存储用户的邮箱, 用来校验该用户是否已存在
    2. email(Django提供字段): 邮箱, 只用来存储邮箱
    3. nick_name: 用户名字, 仅用来表示用户名字, 允许为空
    4. image: 用户头像(该博客中没暂没使用到), 允许为空
    5. add_time: 用户注册的时间, 默认为创建用户时的时间
    6. is_start: 激活状态, 默认未激活
    """
    nick_name = models.CharField(max_length=20, verbose_name='用户昵称',null=True, blank=True)
    image = models.ImageField(upload_to='user/%y/%m/%d', verbose_name='头像', max_length=200, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    is_start = models.BooleanField(default=False, verbose_name='是否激活')
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'UserProfile'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
class VerifyCodeEmail(models.Model):
    """
    验证表: 用来对用户激活时做处理
    1. email: 用户邮箱
    2. code: 发送给邮箱的验证码
    3. code_type: 邮箱的类型, 可以在注册, 重置等功能中
    4. add_time: 发送验证码的时间, 默认发送的时间
    """
    email = models.EmailField(max_length=30, verbose_name='用户邮箱')
    code = models.CharField(max_length=128, verbose_name='验证码')
    code_type = models.CharField(max_length=100,choices=(('1', 'register'), ('2', 'reset'),('3', 'changeemail'), ('4', 'sendpwd')),verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    def __str__(self):
        return self.code
    class Meta:
        db_table = 'VerifyCodeEmail'
        verbose_name = '验证码信息表'
        verbose_name_plural = verbose_name