from django.shortcuts import render, redirect
from . import models
# Create your views here.


def home(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request, 'first_app/home.html', {'student': student})


def delete_student(request, roll):
    student = models.Student.objects.get(pk=roll).delete()
    # print(student)
    return redirect('homepage')
