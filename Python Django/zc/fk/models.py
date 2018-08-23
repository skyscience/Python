from django.db import models

# Create your models here.
class fkInfo(models.Model):
    fid = models.CharField(max_length=20)       #游戏ID
    fdate = models.DateTimeField()                      #提交时间
    fcontact = models.CharField(max_length=22)   #联系方式
    fcontent = models.CharField(max_length=400)  #内容
