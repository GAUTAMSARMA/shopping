from django.urls import path
from app3.views import *
app_name='everything'
urlpatterns=[
    path('g3/',g3,name='g3')
]