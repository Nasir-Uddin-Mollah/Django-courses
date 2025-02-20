from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
# Create your views here.


def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=10)
    response.set_cookie(
        'name', 'karim', expires=datetime.utcnow()+timedelta(days=1))
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})


def del_cookie(request):
    response = render(request, 'del_cookie.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    # data = {
    #     'name': 'nasir',
    #     'age': 24,
    #     'language': 'Bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'nasir'
    return render(request, 'home.html')


def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'guest')
        request.session.modified = True
        return render(request, 'get_session.html', {'name': name})
    else:
        return HttpResponse('Your session has been expired. Login again')


def del_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'del_session.html')
