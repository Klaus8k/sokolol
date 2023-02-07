from django.db import models
import datetime

# Create your models here.
class Solvent_model(models.Model):
    date = models.DateField(verbose_name='date', auto_now_add=True)
    type = models.CharField('type', max_length=20)
    cost = models.IntegerField('cost')

    def __str__(self) -> str:
        return f'Дата изменеия: {self.date}, Материал: {self.type}, Цена за единицу: {self.cost} руб.'

# class Solvent_orders(models.Model):
#     date = models.DateField(verbose_name='order_date', auto_now_add=True)
#     type = models.CharField('type', max_length=20)
#     width = models.FloatField(verbose_name='width')
#     higth = models.FloatField(verbose_name='higth')
#     cost_this = models.IntegerField(verbose_name='cost_this')