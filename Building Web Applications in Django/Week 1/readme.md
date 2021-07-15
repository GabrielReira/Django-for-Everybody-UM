This week I learned about the definition of Model, View and Controller in Django, the overall structure of a Django application, a data model in Django, the way migration works in Django, and explored my app's model admin interface.

Reference sources:

- https://www.dj4e.com/assn/dj4e_tut02.md
- https://www.dj4e.com/lectures/DJ-02-Model-Single.txt
- https://docs.djangoproject.com/en/3.0/intro/tutorial02/
- https://docs.djangoproject.com/en/3.2/ref/models/fields/

---

## Part 1

All lines below are the commands that I used in the **PythonAnywhere** console for this week's first activity. All configuration of the virtual environment was set up in the [first course](https://github.com/GabrielReira/Django-for-Everybody-UM/tree/main/Web%20Application%20Technologies%20and%20Django).

```console
$ cd dj4e-samples
$ workon django3
$ pip3 install -r requirements.txt
$ python3 manage.py check
$ python3 manage.py makemigrations
```

### Resetting database

```console
$ rm db.sqlite3
$ python3 manage.py migrate
```

### Starting Django shell

```py
$ python3 manage.py shell
>>> from users.models import User
>>> u = User(name='Kristen', email='kf@umich.edu')
>>> u.save()
>>> u = User(name='Chuck', email='csev@umich.edu')
>>> u.save()
>>> u = User(name='Colleen', email='cvl@umich.edu')
>>> u.save()
>>> u = User(name='Ted', email='ted@umich.edu')
>>> u.save()
>>> u = User(name='Sally', email='a2@umich.edu')
>>> u.save()
```

### Retrieving and updating data from database

```py
>>> User.objects.values()
<QuerySet [{'id': 1, 'name': 'Kristen', 'email': 'kf@umich.edu'}, {'id': 2, 'name': 'Chuck', 'email': 'csev@umich.edu'}, {'id': 3, 'name': 'Colleen', 'email': 'cvl@umich.edu'}, {'id': 4, 'name': 'Ted', 'email': 'ted@umich.edu'}, {'id': 5, 'name': 'Sally', 'email': 'a2@umich.edu'}]>

>>> User.objects.filter(email='csev@umich.edu').values()
<QuerySet [{'id': 2, 'name': 'Chuck', 'email': 'csev@umich.edu'}]>

>>> User.objects.filter(email='ted@umich.edu').delete()
(1, {'users.User': 1})
>>> User.objects.values()
<QuerySet [{'id': 1, 'name': 'Kristen', 'email': 'kf@umich.edu'}, {'id': 2, 'name': 'Chuck', 'email': 'csev@umich.edu'}, {'id': 3, 'name': 'Colleen', 'email': 'cvl@umich.edu'}, {'id': 5, 'name': 'Sally', 'email': 'a2@umich.edu'}]>

>>> User.objects.filter(email='csev@umich.edu').update(name='Charles')
1
>>> User.objects.filter(id=2).values()
<QuerySet [{'id': 2, 'name': 'Charles', 'email': 'csev@umich.edu'}]>

>>> User.objects.values().order_by('email')
<QuerySet [{'id': 5, 'name': 'Sally', 'email': 'a2@umich.edu'}, {'id': 2, 'name': 'Charles', 'email': 'csev@umich.edu'}, {'id': 3, 'name': 'Colleen', 'email': 'cvl@umich.edu'}, {'id': 1, 'name': 'Kristen', 'email': 'kf@umich.edu'}]>
>>> User.objects.values().order_by('-name')
<QuerySet [{'id': 5, 'name': 'Sally', 'email': 'a2@umich.edu'}, {'id': 1, 'name': 'Kristen', 'email': 'kf@umich.edu'}, {'id': 3, 'name': 'Colleen', 'email': 'cvl@umich.edu'}, {'id': 2, 'name': 'Charles', 'email': 'csev@umich.edu'}]>
```

---

## Part 2

At this part I've written a Django application. All commands below were used in the **PythonAnywhere** console. This part is a continuation of the first course's [activity](https://github.com/GabrielReira/Django-for-Everybody-UM/tree/main/Web%20Application%20Technologies%20and%20Django/Week%202).

```console
$ cd django_projects/mysite/
$ python manage.py migrate
```

### Creating models

In my *poll* app I created two models: **Question** and **Choice**. A *Question* has a question and a publication date. A *Choice* has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question. So, I edited the `~/django_projects/mysite/polls/models.py` file.

```py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### Activating models

I configured the `~/django_projects/mysite/mysite/settings.py` file to include the app in my project.

```py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Django needs to be able to create a database schema for this app and create a Python database-access for accessing *Question* and *Choice* objects. So, I ran the the necessary migrations.

```console
$ python manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
$ python manage.py sqlmigrate polls 0001

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
```

### Playing with the API

At this step I was just interacting with the API and exploring the database.

```py
$ python manage.py shell
>>> from polls.models import Choice, Question

# Creating a new Question
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> Question.objects.values()
<QuerySet [{'id': 1, 'question_text': "What's new?", 'pub_date': datetime.datetime(2021, 7, 13, 23, 31, 42, 511976, tzinfo=<UTC>)}]>

# Changing values
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.values()
<QuerySet [{'id': 1, 'question_text': "What's up?", 'pub_date': datetime.datetime(2021, 7, 13, 23, 31, 42, 511976, tzinfo=<UTC>)}]>
```

### Improving models return

I edited the `~/django_projects/mysite/polls/models.py` file again by adding a `__str__()` method to both models and some more stuff.

```py
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
```

### Restarting and playing again

I saved the *models* file changes and started a new Python interactive shell.

```console
$ cd django_projects/mysite/
$ python manage.py check
$ python manage.py shell
```

Making sure the method is working.

```py
>>> from polls.models import Choice, Question
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
```

There are a lot of ways to lookup data with Django.

```py
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>
>>> Question.objects.get(pk=1)
<Question: What's up?>

>>> from django.utils import timezone
>>> current_year = timezone.now().year

>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True
```

Creating three choices for the question.

```py
>>> q.choice_set.all()
<QuerySet []>
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
```

Choices objects have API access to their related Question and vice versa.

```py
>>> c.question
<Question: What's up?>
>>> q.question
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Question' object has no attribute 'question'

>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3
```

It can be used double underscores to separate relationships.

```py
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
```

Deleting one of the choices.

```py
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c
<QuerySet [<Choice: Just hacking again>]>
>>> c.delete()
(1, {'polls.Choice': 1})
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>]>
```

### Creating an admin user

Django entirely automates the creation of an admin interfaces for models, so I'm going to create it.

```console
$ cd django_projects/mysite/
$ python manage.py check
$ python manage.py createsuperuser
Username: admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```

Then, I reloaded the app in the *web* tab and the admin interface was already activated at `http://(my-account).pythonanywhere.com/admin/`. I made some adjustments in the `~/django_projects/mysite/polls/admin.py` file to make the *poll* app modifiable in the admin interface.

```py
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

Finally, I reload my app again and explored all the admin interface functionalities.
