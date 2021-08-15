from django.core.files.storage import FileSystemStorage
from xlsx_parser.settings import MEDIA_ROOT
from .database import DB

import openpyxl
import os


def validator(filename:str) -> bool:
    """ Валидация файла """ 
    if filename.endswith('xlsx') or filename.endswith('xls'):
        print("OK")
        return False
    return True


def save_file(file) -> str:
    """ Сохраняет файл локально """ 
    fs = FileSystemStorage()
    path = fs.save(file.name, file)
    return os.path.join(MEDIA_ROOT, path)


def parser(path:str) -> bool:
    """ Парсит файл с переносом данных в бд""" 
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.sheetnames[0]
    worksheet = workbook[sheet]

    db = DB()
    for i, row in enumerate(worksheet.rows):
        line = ''.join([str(i.value) for i in row if i != None]).replace('None', '')
        row_list = line.split(';')
        if i == 0: 
            db.set_header(row_list)
            continue
        try:db.add_to_db(row_list)
        except: return False

    return True
