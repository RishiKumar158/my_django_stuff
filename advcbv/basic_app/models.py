from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=128)
    principal = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('basic_app:detail', kwargs={'pk':self.pk})

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name