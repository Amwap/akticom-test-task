from django.views.generic.base import View
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import *


class Table(View):
    """ Рекурсивное oтображение данных с пагинацией """ 

    def get(self, request):
        data = request.GET
        items = 50
        current_page = 1

        # skipped_pages - колличество промотанных страниц
        # items - Количество элементов
        # current_page - данная страница

        if data.get('current_page') != None: current_page = data['current_page']
        if data.get('items') != None: items = data['items']
        if data.get('skipped_page') != None:
            current_page = abs(int(current_page) + int(data['skipped_page']))


        data = Product.objects.all()
        count_items = data.count()
        paginator = Paginator(data, items)
        page_obj = paginator.get_page(current_page)
        all_pages = page_obj.paginator.num_pages

        if current_page <= 1: 
            current_page = 1
            page_obj = paginator.get_page(current_page)
            all_pages = page_obj.paginator.num_pages

        elif current_page > all_pages: 
            current_page = all_pages

        return render(request, 'table.html', {
            'products': page_obj, 
            'items': items, 
            'all_pages': all_pages, 
            'current_page': current_page,
            'count_items': count_items
            })
