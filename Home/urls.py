from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.home ,name='Home'),
    path('home/', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path("contact/",views.contact, name="contact"),
    path("calculator/",views.calculator, name="calculator"),
    path("scams/",views.scams, name="scams"),
    path("sip_calculator/",views.sip_calculator, name="sip_calculator"),
    path("mf_calculator/",views.mf_calculator, name="mf_calculator"),
    path("ppf_calculator/",views.ppf_calculator, name="ppf_calculator"),
    path("swp_calculator/",views.swp_calculator, name="swp_calculator"),
]
