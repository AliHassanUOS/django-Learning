from django.urls import path

from newapp1 import views


urlpatterns = [

    path("newapp1/",views.new_app_fun,name='newapp'),
    



]
