from django.urls import path
from myapp import views

urlpatterns = [
    path('<str:name>/', views.index, name='index' ),
]