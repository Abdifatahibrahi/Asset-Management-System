from django.contrib import admin
from .models import Furniture, FurnitureType, Vehicle, VehicleType, Electronic, ElectronicType, Land, Location

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('serial_no', 'type', 'date', 'time', 'initial_value', 'depreciation_rate', 'current_value',)
admin.site.register(Furniture, FurnitureAdmin)

class FurnitureTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
admin.site.register(FurnitureType, FurnitureTypeAdmin)



class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'type', 'date')
admin.site.register(Vehicle, VehicleAdmin)

class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
admin.site.register(VehicleType, VehicleTypeAdmin)


class ElectronicAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'type', 'date', 'time', 'initial_value', 'depreciation_rate', 'current_value',)
admin.site.register(Electronic, ElectronicAdmin)

class ElectronicTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
admin.site.register(ElectronicType, ElectronicTypeAdmin)



class LandAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date', 'time', 'initial_value', 'apreciation_rate', 'current_value',)
admin.site.register(Land, LandAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)
admin.site.register(Location, LocationAdmin)