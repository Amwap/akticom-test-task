from django.db.models import Model, TextField, CharField, ForeignKey
from django.db import models
from django.db.models.fields import BooleanField, IntegerField


class Level(models.Model):
    """ Уровни """ 
    name = CharField('Наименование', max_length=10)
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

class Level1(Level): pass
class Level2(Level): pass
class Level3(Level): pass


class Unit(models.Model):
    name = ("Наименование")
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class Product(models.Model):
    code = CharField("Код", max_length=10, unique=True)
    name = TextField("Наименование")
    level1 =  ForeignKey(Level1, on_delete=models.PROTECT)
    level2 =  ForeignKey(Level2, on_delete=models.PROTECT)
    level3 =  ForeignKey(Level3, on_delete=models.PROTECT)
    price = IntegerField("Цена")
    priceSP = IntegerField("Цена СП")
    count = IntegerField("Количество")
    properties = TextField("Поля свойств")
    joint_purchases = TextField("Поля свойств")
    unit = ForeignKey(Unit, on_delete=models.PROTECT)
    picture = CharField("Код", max_length=50)
    on_general = BooleanField('Выводить на главной')
    def __str__(self) -> str:
        return f'{self.code} {self.name}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"