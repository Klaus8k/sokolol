import datetime

from django.db import models


# Create your models here.
class Solvent_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    type = models.CharField('type', max_length=20)
    cost = models.IntegerField('cost')

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

    def __str__(self) -> str:
        if self.duplex:
            duplex = '4+4'
        else:
            duplex = '4+0'
        return f'{self.formatX}x{self.formatY}мм, {self.density}г/м, {self.pressrun}шт, {duplex}, цена: {self.cost} руб.'

