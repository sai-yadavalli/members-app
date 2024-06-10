from django.db import models


# Create your models here.
class Class(models.Model):
    year = models.IntegerField(default=2020)

    def __str__(self):
        return str(self.year)


software_engineering = 'Software Engineering'
computer_science = 'Computer Science'
data_science = 'Data Science'
business = 'Business'
engineering = 'Engineering'
architecture = 'Architecture'

disciples_choices = [
    (software_engineering, software_engineering),
    (computer_science, computer_science),
    (data_science, data_science),
    (business, business),
    (engineering, engineering),
    (architecture, architecture),
]


class Disciple(models.Model):
    degree = models.CharField(max_length=255, choices=disciples_choices, default="degree")

    def __str__(self):
        return self.degree


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    enrollment_year = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, default=2020)
    college_degree = models.ForeignKey(Disciple, on_delete=models.SET_NULL, null=True, default="degree")

    def __str__(self):
        return self.name
