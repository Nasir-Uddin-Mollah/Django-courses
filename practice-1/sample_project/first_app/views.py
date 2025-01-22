from django.shortcuts import render
import datetime
# Create your views here.


def home(request):
    dic = {'Name': 'Nasir', 'Age': 24, 'Profession': 'Student',
           'Friends': ['Risan', 'Sayem', 'Rahim'],
           'Courses': 
           [   {
               'Name': 'Python',
               'Price': 2000
               },
               {
               'Name': 'Django',
               'Price': 4000
                },
               {
               'Name': 'JavaScript',
               'Price': 3000
                }
            ],
            'date': datetime.datetime.now(),
            'time': datetime.datetime.now().time(),
            'birthdate' : datetime.datetime(2000,3,9),
            'val': '< > & " '
           }

    return render(request, 'first_app/index.html', dic)
