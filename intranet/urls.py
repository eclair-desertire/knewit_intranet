from os import name
from django.urls import path
from . import views
urlpatterns = [
    path('test/', views.test_page, name='test_page'),
    path('',views.main_page,name='main.page'),
]