from django.contrib import admin
from blogs.models import Banner, Post, BlogCategory, Tags, FriendlyLink

admin.site.register(Banner)
# admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Tags)

admin.site.register(FriendlyLink)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/editor/kindeditor-all.js',
            'js/editor/config.js',
        )
admin.site.register(Post, PostAdmin)
