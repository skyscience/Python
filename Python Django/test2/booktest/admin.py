from django.contrib import admin
from .models import BookInfo,HeroInfo


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'gender', 'hcontent']

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'btitle', 'bpub_date']  
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10    
    inlines = [HeroInfoInline]




admin.site.register(BookInfo, BookInfoAdmin)  
admin.site.register(HeroInfo,HeroInfoAdmin)