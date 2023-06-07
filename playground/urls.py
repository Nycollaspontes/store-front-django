from django.urls import path 
from . import views 

#Url configuration 
urlpatterns = [
    path("hello/" , views.say_hello)
]