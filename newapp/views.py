from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def fun1(request):

    a = 3
    b = 4
    c = a+b
    d = a-b
    take_list = [1,2,3]

    for i in take_list:
        show = i


    return render(request, "newapp\home.html", {"c" : c , "d" : d, "show":show})
