from django.db import models

def ChairPref(number):
        string_x = 'CH'+ str(number)
        return string_x
def CupboardPref(number):
        string_x = 'CB'+ str(number)
        return string_x
        
def TablePref(number):
        string_x = 'TB'+ str(number)
        return string_x
    
class FurnitureType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"


class Furniture(models.Model):
    type = models.ForeignKey(FurnitureType, on_delete=models.CASCADE)
    serial_no = models.AutoField(auto_created=True, primary_key=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    initial_value = models.IntegerField()
    depreciation_rate = models.DecimalField(max_digits=100, decimal_places=2)
    current_value = models.IntegerField()

    def __str__(self):
        return f"{self.serial_no} {self.type}"
    
    # def save(self, *args, **kwargs):
    #     if self.type == "Chair":
    #         self.serial_no = ChairPref(self.serial_no)
    #     elif self.type == "Table":
    #         self.serial_no = TablePref(self.serial_no)
    #     else:
    #         self.serial_no = ChairPref(self.serial_no)
    #     super(Furniture, self).save(*args, **kwargs)
    
class VehicleType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"
    

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=20)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    initial_value = models.IntegerField()
    depreciation_rate = models.DecimalField(decimal_places=2, null=True, max_digits=5)
    current_value = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.number_plate} {self.type}"
    
    
    # def save(self, *args, **kwargs):
    #         self.id = int('VEH' + str(self.id))
    #         return super(Vehicle, self).save(*args, **kwargs)
    


    
    # Electronics
class ElectronicType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"
    
class Electronic(models.Model):
    serial_number = models.AutoField(auto_created=True, primary_key=True)
    type = models.ForeignKey(ElectronicType, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    initial_value = models.IntegerField()
    depreciation_rate = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    current_value = models.IntegerField(null=True)
    
    
    def __str__(self):
        return f"{self.serial_number} {self.type}"
    
    

    

# Land\
    
class Location(models.Model):
    location = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.location}"


class Land(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    initial_value = models.IntegerField()
    apreciation_rate = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    current_value = models.IntegerField(null=True)
    
    
    def __str__(self):
        return f"{self.name} {self.location}"