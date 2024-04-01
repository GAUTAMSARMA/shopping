from django.urls import path
from mobile.views import *
app_name='something'
urlpatterns=[
    path('samsung/',samsung,name='samsung'),
]