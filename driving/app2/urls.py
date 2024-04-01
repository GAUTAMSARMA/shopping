from django.urls import path
from app2.views import *
app_name='EVERYTHING'
urlpatterns=[
    path('g2/',g2,name='g2')
]