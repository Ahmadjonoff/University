from django.db import models

class Product(models.Model):
    firma = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    model = models.SmallIntegerField()

    def __str__(self):
        return f'{self.type} model = {self.model}'

class PC(models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    RAM = models.SmallIntegerField()
    HD = models.SmallIntegerField()
    narx = models.IntegerField()

    def __str__(self):
        return str(self.model)

class Printer(models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    rangli = models.BooleanField()
    narx = models.IntegerField()

    def __str__(self):
        return str(self.model)

class Laptop(models.Model):
    model = models.ForeignKey(Product, on_delete=models.CASCADE)
    RAM = models.SmallIntegerField()
    HD = models.SmallIntegerField()
    narx = models.IntegerField()
    ekran = models.CharField(max_length=10)

    def __str__(self):
        return str(self.model)