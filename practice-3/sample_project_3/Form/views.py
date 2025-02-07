from django.shortcuts import render
from . forms import Exampleform
# Create your views here.


def myform(request):
    if request.method == 'POST':
        form = Exampleform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = Exampleform()
    return render(request, 'form.html', {'form': form})
