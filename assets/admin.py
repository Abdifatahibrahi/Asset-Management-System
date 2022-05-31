from django.contrib import admin
from .models import Furniture, FurnitureType

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('serial_no', 'type', 'date', 'time',)
admin.site.register(Furniture, FurnitureAdmin)

class FurnitureTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
admin.site.register(FurnitureType, FurnitureTypeAdmin)


# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'gender','mobile', 'address')
# admin.site.register(Patient, PatientAdmin)


# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'doctor', 'patient', 'date', 'time')
# admin.site.register(Appointment, AppointmentAdmin)
