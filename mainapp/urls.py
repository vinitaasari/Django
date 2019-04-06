from django.urls import path
from . import views

urlpatterns =[
    path("home/",views.home),
    path("about/",views.about),
    path("contact/",views.contact),
    path("save",views.save),
    path("login",views.login),
    path("test/",views.test),

    ]