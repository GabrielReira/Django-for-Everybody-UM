from django.http import HttpResponse

def cookie(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits >= 7:
        del(request.session['num_visits'])
    res = HttpResponse('view count=' + str(num_visits))
    res.set_cookie('dj4e_cookie', '6642423e', max_age=1000)

    return res
