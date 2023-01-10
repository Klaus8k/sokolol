from django.db import models

# Create your models here.
class Solvent(models.Model):
    date = models.TimeField(verbose_name='date', auto_now_add=True)
    type = models.CharField('type', max_length=20)
    cost = models.IntegerField('cost')

    def __str__(self) -> str:
        return f'{self.date} {self.type} {self.cost}'
