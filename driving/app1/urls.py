from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('g1/',g1,name='g1')
]