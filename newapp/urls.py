from django.urls.conf import path

from newapp import views
urlpatterns = [

    path("",views.fun1,name="fun1")

]
