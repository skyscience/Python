from django.contrib import admin
from .models import BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub_date'],
    list_filter = ['btitle']

admin.site.register(BookInfo)

