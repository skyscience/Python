from django.db import models

# Create your models here.

class Bookinfo (models.Model):
    btitle = models.CharField(max_length=30)
    bdate = models.DateTimeField()

    def __str__(self):
        return '%d' % self.pk


class Heroinfo(models.Model):
    hname = models.CharField(max_length=20)
    hgander = models.BooleanField()

    def __str__(self):  
        return '%d' % self.pk