from myapp.models import Product
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .static import save_file, parser, validator


def page(request):
    return render(request, 'index.html')


def data_parser(request):
    print(request.FILES, 'HERE')
    file = request.FILES['table']
    if validator(file.name): return redirect('/')
    path = save_file(file)
    status = parser(path)
    if status != True: return redirect('/')
    return redirect('/data_view/')

# def data_view(request):
#     products = Product.objects.all
#     return render(request, 'table.html', {"products": products})