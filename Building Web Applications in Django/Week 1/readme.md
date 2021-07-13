This week I learned about the definition of Model, View and Controller in Django, the overall structure of a Django application, a data model in Django, the way how migration works in Django and I explore the model admin interface of it.

Reference sources:

- https://www.dj4e.com/lectures/DJ-02-Model-Single.txt
- https://docs.djangoproject.com/en/3.0/intro/tutorial02/
- https://docs.djangoproject.com/en/3.2/ref/models/fields/

---

## Part 1

All lines bellow are the commands that I used in **PythonAnywhere** console for the first activity of this week. All configuration of the virtual environment was set up on the [first course](https://github.com/GabrielReira/Django-for-Everybody-UM/tree/main/Web%20Application%20Technologies%20and%20Django).

```console
$ cd dj4e-samples
$ workon django3
$ pip3 install -r requirements.txt
$ python3 manage.py check
$ python3 manage.py makemigrations
```

### Reseting database

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
