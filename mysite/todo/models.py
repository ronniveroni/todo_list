from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    LOAN_STATUS = (
        ('n', 'Not started'),
        ('p', 'In progress'),
        ('c', 'Completed'),
    )

    status = models.CharField(verbose_name="Status", max_length=1, choices=LOAN_STATUS, blank=True, default="n")



    def __str__(self):
        return f'{self.name} {self.content} {self.user} {self.date}'