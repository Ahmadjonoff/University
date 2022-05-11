from django.db import models

class Speciality(models.Model):
    name = models.CharField(max_length = 30)
    code = models.SmallIntegerField()
    start_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    degree = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.degree})'

class Subject(models.Model):
    name = models.CharField(max_length = 20)
    specialities = models.ForeignKey(Speciality, on_delete = models.CASCADE)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name