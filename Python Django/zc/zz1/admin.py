from django.contrib import admin
from .models import BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','player','money','date']
    list_filter = ['player']

admin.site.register(BookInfo,BookInfoAdmin)