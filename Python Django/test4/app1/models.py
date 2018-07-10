from django.db import models
from ckeditor.fields import RichTextField

class AreaInfo(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    aPArea = models.ForeignKey('AreaInfo', null=True,on_delete=models.PROTECT)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()

class TestModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    book=models.ForeignKey(BookInfo, null=True,on_delete=models.PROTECT)    
    hcontent=models.CharField(max_length=1000)    
    isDelete=models.BooleanField(default=False)
