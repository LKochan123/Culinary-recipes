### About project:
Culinary recipes project is a blog about my grandma recipes. Users can see it on responsive website, comment and do some other stuff.

### Technologies:
  - Django 4.1 
  - Python 3.10
  - Bootstrap 5.0 
  - HTML/CSS & JavaScript

### Page capabilities:
  - Setting an account (optional - for more feateures)
  - Commenting posts
  - Adding posts recipes to favourite section
  - Customized admin panel for owner of a blog 
  - Changing color of website 
  
### How to run this project localy?
1. Git clone the repository
2. Set up a python virtual environment
3. Run this command:
```
$ pip install -r requirements.txt
```
4. Generate key on <a href="https://miniwebtool.com/django-secret-key-generator/" target="_blank"> this site</a> and assign it to variable SECRET_KEY in settings.py file.
5. Run this commands:
```
$ python manage.py createsuperuser
$ python manage.py makemigrations
$ python manage.py migrate
```
6. Open localhost:8000 on your browser. 
7. Add '/admin' to your URL and login with your superuser account. Now you can add recipes and create your own culinary blog. 
