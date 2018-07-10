from django.db import models

class BookInfoManagr(models.Manager):
    def get_queryset(self):
        return super(BookInfoManagr,self).get_queryset().filter(pk=2)
    
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    book = models.Manager()
    book2 = BookInfoManagr()#会覆盖类的属性

    @classmethod
    def create(cls,title,pub_date):
        # b = cls(btitle,bpub_date):
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('Bookinfo',on_delete=models.PROTECT)

        