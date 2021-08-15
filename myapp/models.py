from django.db.models import TextField, CharField, ForeignKey
from django.db import models
from django.db.models.fields import BooleanField, FloatField, IntegerField


class BaseLevel(models.Model):
    """ Родитель уровней """ 
    name = CharField('Наименование', max_length=10)
    def __str__(self) -> str:
        return self.name

class Level1(BaseLevel):
    class Meta:
        verbose_name = "Уровень1"
        verbose_name_plural = "Уровень1"

class Level2(BaseLevel):
    class Meta:
        verbose_name = "Уровень2"
        verbose_name_plural = "Уровень2"

class Level3(BaseLevel):
    class Meta:
        verbose_name = "Уровень3"
        verbose_name_plural = "Уровень3"


class Unit(models.Model):
    """ Единицы измерения""" 
    name = CharField("Наименование", max_length=10, default='')
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"


class Product(models.Model):
    code = CharField("Код", max_length=10, unique=True)
    name = TextField("Наименование")
    level1 = ForeignKey(Level1, on_delete=models.PROTECT, verbose_name='Уровень 1')
    level2 = ForeignKey(Level2, on_delete=models.PROTECT, verbose_name='Уровень 2')
    level3 = ForeignKey(Level3, on_delete=models.PROTECT, verbose_name='Уровень 3')
    price = IntegerField("Цена")
    priceSP = IntegerField("Цена СП")
    count = FloatField("Количество")
    unit = ForeignKey(Unit, on_delete=models.PROTECT, verbose_name='Единица измерения')
    properties = TextField("Поля свойств")
    joint_purchases = TextField("Совместные покупки")
    picture = CharField("Картинка", max_length=50)
    on_general = BooleanField('Выводить на главной', default=False)
    note = models.TextField("Описание")
    
    def __str__(self) -> str:
        return f'{self.code} {self.name}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"