from django.db import models

class Furniture(models.Model):
    serial_no = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    initial_value = models.IntegerField()
    depreciation_rate = models.DecimalField(max_digits=100, decimal_places=2)
    current_value = models.IntegerField()

    def __str__(self):
        return f"{self.serial_no} {self.type}"
    
class FurnitureType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"
    

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    date = models.DateField()
    initial_value = models.IntegerField(null=True)
    depreciation_rate = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    current_value = models.IntegerField(null=True)
    
    def __str__(self):
        return f"{self.number_plate} {self.type}"

class VehicleType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"