from django.db import models
class Worker (models.Model):
    name = models.CharField(max_length=20,blank=True)
    second_name = models.CharField(max_length=35,blank=True)
    def __str__(self):
        return f'{"Имя:"}{self.name}{"///Фамилия:"}{self.second_name}'

# Create your models here.
