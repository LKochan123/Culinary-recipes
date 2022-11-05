from django.contrib import admin
from .models import Post, Ingridient, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post",)
    list_display = ("post",)


admin.site.register(Post, PostAdmin)
admin.site.register(Ingridient)
admin.site.register(Comment, CommentAdmin)
