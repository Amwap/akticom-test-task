from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from openpyxl.worksheet import worksheet
from xlsx_parser.settings import MEDIA_ROOT
import os
import openpyxl

def page(request):
    return render(request, 'index.html')

def parser(request):
    myfile = request.FILES['table']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    workbook = openpyxl.load_workbook(os.path.join(MEDIA_ROOT, filename))
    sheet = workbook.sheetnames[0]
    worksheet = workbook[sheet]
    for i, row in enumerate(worksheet.rows):
        if i == 10: break
        line = ''.join([str(i.value) for i in row if i != None]).replace('None', '')
        row_list = line.split(';')
        print(row_list)

    return HttpResponse('ok')
