from django.db import models

class Furniture(models.Model):
    serial_no = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.serial_no} {self.type}"
    
class FurnitureType(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.type}"

# class Patient(models.Model):
#     name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=30)
#     mobile = models.IntegerField(null=True)
#     address = models.TextField()

#     def __str__(self):
#         return self.name

# class Appointment(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()

#     def __str__(self):
#         return f"{self.doctor.name}, {self.patient.name}"


