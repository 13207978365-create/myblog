import time
import hashlib
from django.core.mail import send_mail
from django.conf import settings
from users.models import VerifyCodeEmail
def make_sign():
    """
    生成一个加密字符串
    时间戳+Django秘钥 通过md5加密
    """
    times = str(time.time())
    sign_str = times + settings.SECRET_KEY
    md5 = hashlib.md5()
    md5.update(sign_str.encode())
    sign = md5.hexdigest()
    return sign

def send_verify_email(to_email):
    """
    发送验证邮件
    为了保证唯一性, 该邮件只能是某一用户的激活邮件, 该邮件后面的参数通过加密来得到一个字符串
    """

    sign = make_sign()
    verify_url = '点击链接激活账号\n http://127.0.0.1:8000/user_active?sign = ' + sign
    # 生成一个验证的对象, 将发送的数据存储进去, 在激活的时候去验证
    verify_code = VerifyCodeEmail()
    verify_code.email = to_email
    verify_code.code = sign
    verify_code.code_type = 1
    verify_code.save()
    subject = "邮箱验证"
    html_message = '<p>尊敬的用户您好！</p>' \
                   '<p>感谢您使用此网站。</p>' \
                   '<p>您的邮箱为：%s 。请点击此链接激活您的邮箱：</p>' \
                   '<p><a href="%s">%s<a></p>' % (to_email, verify_url,
                                                  verify_url)
    # 调用Django提供的方法来发送邮件
    send_mail(subject, "", settings.EMAIL_FROM, [to_email], html_message=html_message)