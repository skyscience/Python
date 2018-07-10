from django.db import models

class AreaInfo(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    aPArea = models.ForeignKey('AreaInfo', null=True,on_delete=models.PROTECT)