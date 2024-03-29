from django.db import models


# Create your models here.
class Solvent_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    type_prod = models.CharField('type_prod', max_length=20, default='banner')  
    cost = models.IntegerField('cost')
    type_order = models.CharField('solvent', max_length=20, default='solvent')

    def __str__(self) -> str:
        return f'Дата: {self.date.strftime("%m/%d/%y %H:%M:%S")}, Материал: {self.type_prod}, Цена за m2: {self.cost} руб.'


class Offset_model(models.Model):
    date = models.DateTimeField(verbose_name='date', auto_now_add=True)
    # Наполнить модель правильными параметрами
    formatX = models.IntegerField()
    formatY = models.IntegerField()
    density = models.IntegerField()
    pressrun = models.IntegerField()
    duplex = models.BooleanField()
    cost = models.IntegerField(default=None)
    type_order = models.CharField('offset', max_length=20, default='offset')


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
