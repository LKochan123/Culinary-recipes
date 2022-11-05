from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Ingridient(models.Model):
    ingridient = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ingridient}"


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="posts", null=True)
    short_description = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    ingridients = models.ManyToManyField(Ingridient)
    favourites = models.ManyToManyField(
        User, related_name='favourite', blank=True)
    objects = models.Manager()
    newmanager = NewManager()

    def __str__(self):
        return f"{self.title}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()

    def __str__(self):
        return self.user


class Comment(models.Model):
    nickname = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
