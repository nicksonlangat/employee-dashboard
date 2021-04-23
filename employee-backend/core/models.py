from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    department=models.CharField(max_length=20)
    salary=models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.name