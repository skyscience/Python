from django.contrib import admin

# Register your models here.
from .models import fkInfo

class fkInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','fid','fdate']

admin.site.register(fkInfo,fkInfoAdmin)