import datetime

from django.db import models


# Create your models here.
class Solvent_model(models.Model):
    date = models.DateField(verbose_name='date', auto_now_add=True)
    type = models.CharField('type', max_length=20)
    cost = models.IntegerField('cost')

    def __str__(self) -> str:
        return f'Дата изменеия: {self.date}, Материал: {self.type}, Цена за единицу: {self.cost} руб.'

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
        return f'{self.formatX}X{self.formatY}мм, {self.density}г/м, {self.pressrun}шт, duplex{self.duplex}, цена: {self.cost}'

