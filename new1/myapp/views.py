from django.shortcuts import render

# Create your views here.
def index(request, name):
    dict = {"name":name}
    return render(request, 'myapp/index.html', context=dict)
