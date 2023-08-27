from django.shortcuts import render
from myapp.models import Menu
# Create your views here.


def index(request):
    menu = Menu.objects.all()
    dict = {'menu':menu}
    return render(request, 'myapp/index.html', context=dict)