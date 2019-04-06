from django.urls import path,include

urlpatterns =[
    path("gits/",include("mainapp.urls"))
]