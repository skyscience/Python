from django.contrib import admin
from .models import Bookinfo,Heroinfo
# from .models import 

class BookinfoAdmin(admin.ModelAdmin):
    search_fields = ['btitle'],
    list_filter = ['btitle']
    list_display = ['pk', 'btitle', 'bdate']
    list_per_page = 10


admin.site.register(Bookinfo)
admin.site.register(Heroinfo)