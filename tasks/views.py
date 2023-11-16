from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def college(request):
    return HttpResponse("'College' view")


def professional(request):
    return HttpResponse("'Professional' view")


def groceries(request):
    return HttpResponse("'Groceries' view")


def category(request, param):
    if param == 'college':
        ret = ("'College' view")
    elif param == 'professional':
        ret = ("'Professional' view")
    elif param == 'groceries':
        ret = ("'Groceries' view")
    else:
        return HttpResponseNotFound('Rota não encontrada')

    return HttpResponse(ret)
