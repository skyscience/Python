from django.db import models
from datetime import datetime
# Create your models here.


from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    nikename = models.CharField('昵称', max_length=20, default='')

class EmailVerifyRecord(models.Model):
    code = models.CharField(verbose_name='验证码', max_length=50,default='')
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(verbose_name="验证码类型", choices=(("register",u"注册"),("forget","找回密码"), ("update_email","修改邮箱")), max_length=30)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
