from django.db import models
# Create your models here.
class BookInfo(models.Model):
    player = models.CharField(max_length=20) #玩家名
    date = models.DateTimeField()           #赞助时间
    money = models.FloatField(default=0)  #赞助金额