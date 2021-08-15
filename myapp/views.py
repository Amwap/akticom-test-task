from myapp.models import Product
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .static import save_file, parser, validator, DB


def page(request):
    """ Вью для индексной страницы"""
    return render(request, 'index.html')


def data_parser(request):
    """ Валидация файла с редиректами """
    file = request.FILES['table']
    if validator(file.name): return redirect('/')
    path = save_file(file)
    status = parser(path)
    if status != True: return redirect('/')
    return redirect('/data_view/')


def wipe_data(request):
    """ Удаление данных о продукции """
    DB().wipe_data()
    return redirect('/')
