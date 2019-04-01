from django.db import models


# Create your models here.
class Phone(models.Model):
    model = models.CharField(verbose_name='Модель', max_length=50)
    display = models.FloatField(verbose_name='Диагональ экрана', max_length=5)
    resolution = models.CharField(verbose_name='Разрешение экрана', max_length=20)
    camera = models.CharField(verbose_name='Камера (Мп)', max_length=50)
    memory = models.PositiveIntegerField(verbose_name='Память (Гб)')
    phone_os = models.CharField(verbose_name='Операционная система', max_length=20)
    price = models.PositiveIntegerField(verbose_name='Цена')


class Samsung(Phone):
    extra_memory = models.PositiveIntegerField(verbose_name='Карта памяти (Гб)')


class Apple(Phone):
    lightning = models.BooleanField(verbose_name='Разъем Lightning', default=True)

