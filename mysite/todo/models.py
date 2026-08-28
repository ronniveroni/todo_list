from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    LOAN_STATUS = (
        ('n', 'Not started'),
        ('p', 'In progress'),
        ('c', 'Completed'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=LOAN_STATUS, blank=True, default="n")


    def __str__(self):
        return f'{self.date.strftime("%Y-%m-%d %H:%M")}, {self.name} {self.tags}, {self.status}'