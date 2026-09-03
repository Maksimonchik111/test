from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='task_name')
    text = models.TextField(verbose_name='task_text')

    def __str__(self):
        return self.name