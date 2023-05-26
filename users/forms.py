from django import forms

class RegisterForm(forms.Form):
    """
    用户注册的表单: 当用户点击注册时, 可以通过我们所写的表单字段来对数据进行校验
    email: 用来校验用户提交的邮箱, EmailField(forms中定义的邮箱类型), required(保存
    用户提交的数据不能为空), error_messages(如果有错误, 则根据字典中错误的key来提示对应信
    息)
    password: 用来校验用户提交的密码, CharField(forms中定义的字符串类型)
    nick_name: 用来校验用户提交的名字
    """
    email = forms.EmailField(required=True, error_messages={'required': '请填写邮箱', 'invalid': '请输入有效的邮箱'})
    password = forms.CharField(required=True, error_messages={'required': '请填写密码'})
    nick_name = forms.CharField(required=True, error_messages={'required': '请填写名字'})