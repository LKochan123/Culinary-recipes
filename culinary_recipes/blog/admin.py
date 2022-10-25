from django.contrib import admin
from .models import Post, Author, Ingridient, Level, Comment

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "country", "e_mail")


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("post", "nickname")
    list_display = ("nickname", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Ingridient)
admin.site.register(Level)
admin.site.register(Comment, CommentAdmin)
