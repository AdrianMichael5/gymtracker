from django.urls import path
from autentication import views

urlpatterns = [
    path('',views.Home,name="Home")


]