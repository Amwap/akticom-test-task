from .models import *


class DB():
    """ """ 
    def __init__(self) -> None:
        self.rows = []


    def set_header(self, header:list):
        """ устанавливает header строки """
        self.header = header
        # dict(zip(self.rows, ))


    def add_to_db(self, line:list):
        """ Парсит список добавляя данные в базу данных""" 
        array = dict(zip(self.header, line))
        levels = self._set_levels(array['Уровень1'], array['Уровень2'], array['Уровень3'])
        def to_int(data):
            if data == '': return 0
            else: return float(data)
            
        Product.objects.get_or_create(
            code = array['Код'],
            name = array['Наименование'],
            level1 = levels[0],
            level2 = levels[1],
            level3 = levels[2],
            price = to_int(array['Цена']),
            priceSP = to_int(array['ЦенаСП']),
            count =  to_int(array['Количество']),
            properties = array['Поля свойств'],
            joint_purchases = array['Совместные покупки'],
            unit = self._set_unit(array['Единица измерения']),
            picture = array['Картинка'],
            on_general = array['Выводить на главной'],
        )



    def _set_unit(self, name:str) -> Unit:
        """ Возвращает объект единицы измерения"""
        unit = Unit.objects.get_or_create(name=name)
        return unit[0]
        

    def _set_levels(self, name1:str, name2:str, name3:str):
        """ Возвращает список объектов уровня """ 
        level1 = Level1.objects.get_or_create(name=name1)
        level2 = Level2.objects.get_or_create(name=name2)
        level3 = Level3.objects.get_or_create(name=name3)
        return level1[0], level2[0], level3[0]
