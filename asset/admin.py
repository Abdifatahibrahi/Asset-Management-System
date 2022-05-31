from django.contrib import admin
from .models import Furniture, FurnitureType, Vehicle, VehicleType

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