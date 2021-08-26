from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def new_app_fun(respone):

    a = "Ali Hassan"
    b = "ahmad Hassan"

    return HttpResponse(f"hello {a} How are you brother ,,,,{b}")


