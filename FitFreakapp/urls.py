from django.urls import path
from . import views

urlpatterns=[
    path('', views.fit, name='fit'),
    path('result/', views.result, name='result')
]