from app1.views import *
from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('first_app1/',first_app1,name='first_app1'),

]