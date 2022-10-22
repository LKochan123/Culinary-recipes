from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from traitlets import default

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


class Level(models.Model):
    level = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.level}"


class Post(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], default=None)
    short_description = models.CharField(max_length=100)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    time_to_prepere_in_minutes = models.PositiveIntegerField(default=None)
    kcal = models.PositiveIntegerField(default=None)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    ingridients = models.ManyToManyField(Ingridient)

    def __str__(self):
        return f"{self.title} {self.date} {self.author}"
