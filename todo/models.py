
from django.db import models


class Todos(models.Model):
    name = models.CharField(max_length=512, verbose_name="todo", null=False, blank=False)
    completed = models.BooleanField(default=False)
    expired = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-expired']
        verbose_name = 'todos'

