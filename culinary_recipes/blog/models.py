from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    e_mail = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Ingridient(models.Model):
    ingridient = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ingridient}"


class Post(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="posts", null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=None)
    short_description = models.CharField(max_length=100)
    time_to_prepere_in_minutes = models.PositiveIntegerField(default=None)
    kcal = models.PositiveIntegerField(default=None)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    ingridients = models.ManyToManyField(Ingridient)

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
