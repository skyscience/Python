from django.db import models
# Create your models here.


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('Bookinfo',on_delete=models.PROTECT) 

    def gender(self):
        if self.hgender:
            return '男'
        else:
            return '女'

    gender.short_description = '性别' #对应的属性