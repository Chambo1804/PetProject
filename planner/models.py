from django.db import models


class delo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Задача')
    content = models.TextField(null=True, blank=True, verbose_name='Описание задачи')
    time = models.DateTimeField(null=True, verbose_name='Время задачи')
    importance = models.SmallIntegerField(null=True, verbose_name='Важность задачи')
    type = models.ForeignKey('Type', null=True, on_delete=models.PROTECT, verbose_name='Тип задачи')

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['time']

class Type(models.Model):

    name = models.CharField(max_length=20, db_index=True, verbose_name='Тип задачи')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Типы задач'
        verbose_name = 'Тип задач'
        ordering = ['name']

# Create your models here.
