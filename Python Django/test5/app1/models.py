from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    
# Create your models here.
class TestModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()