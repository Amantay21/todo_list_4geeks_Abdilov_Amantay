from django.db import models

status_choices = [('new', 'Новая'), ('done', 'Сделано')]
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=3000, verbose_name='Описание')
    completed = models.CharField(max_length=100, default=status_choices[0][0],
                                 verbose_name="Статус", choices=status_choices)
    date_of_completion = models.DateTimeField(verbose_name='Дата выполнения', auto_now_add=True)

    def __str__(self):
        return f'{self.id}. {self.title}'
