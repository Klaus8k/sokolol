import datetime

from django.db import models


class Type_Order(models.Model):
    type_order = models.CharField(unique=True, max_length=20)

    def __str__(self) -> str:
        return self.type_order


# Create your models here.
class Solvent_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    type = models.CharField('type', max_length=20)
    cost = models.IntegerField('cost')
    type_order = models.ForeignKey(
        Type_Order, on_delete=models.CASCADE, default='4', verbose_name='solvent')

    def __str__(self) -> str:
        return f'Дата: {self.date.strftime("%m/%d/%y %H:%M:%S")}, Материал: {self.type}, Цена за m2: {self.cost} руб.'


class Offset_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    # Наполнить модель правильными параметрами
    formatX = models.IntegerField()
    formatY = models.IntegerField()
    density = models.IntegerField()
    pressrun = models.IntegerField()
    duplex = models.BooleanField()
    cost = models.IntegerField(default=None)
    type_order = models.ForeignKey(
        Type_Order, on_delete=models.CASCADE, default='3', verbose_name='offset')

    def __str__(self) -> str:
        if self.duplex:
            duplex = '4+4'
        else:
            duplex = '4+0'
        return f'{self.formatX}x{self.formatY}мм, {self.density}г/м, {self.pressrun}шт, {duplex}, цена: {self.cost} руб.'


class Riso_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    paper_cost_80 = models.IntegerField()
    black_ink_cost = models.IntegerField()
    master_list_cost = models.IntegerField()

    def __str__(self):
        return f'{self.date.strftime("%m/%d/%y %H:%M:%S")} - {self.paper_cost_80} - {self.black_ink_cost} - {self.master_list_cost}'
