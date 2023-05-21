from django.urls import path , include
from .views import *

urlpatterns = [
    path('',index),
    path('index',index),
    path('dashboard/',dashboard),
    path('menu_and_order/', menu_and_order),
    # path('add_order/',receipt),
] 