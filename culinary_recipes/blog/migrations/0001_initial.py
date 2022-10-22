# Generated by Django 4.1.2 on 2022-10-22 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingridient', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image_name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=60)),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
                ('ingridients', models.ManyToManyField(to='blog.ingridient')),
            ],
        ),
    ]