from django.urls import path
from . import views1 
#from views1 import *            
urlpatterns = [
path('',views1.index, name='index'),
]
