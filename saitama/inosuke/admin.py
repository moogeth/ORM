from django.contrib import admin
from .models import Car_Inventory, Car_InventoryAdmin
admin.site.register(Car_Inventory, Car_InventoryAdmin)