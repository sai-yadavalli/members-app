from django.db import models

# Create your models here.
class Class(models.Model):
    year = models.IntegerField(default=2020)
    
    def __str__(self):
        return str(self.year)


class Disciple(models.Model):
    degree = models.CharField(max_length=255, default="degree")
    
    def __str__(self):
        return self.degree
    
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    year = models.ForeignKey(Class, on_delete=models.CASCADE, default=2020)
    degree = models.ForeignKey(Disciple, on_delete=models.CASCADE, default="degree")
    
    def __str__(self):
        return self.name