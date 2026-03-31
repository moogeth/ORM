from django.db import models
from django.contrib import admin
class Car_Inventory(models.Model): 
    No_Plate= models.IntegerField()
    Car_Model = models.CharField(max_length=100)
    Car_Type = models.CharField(max_length=20)
    Mileage = models.IntegerField( )
    Engine_Type = models.CharField(max_length=15)
    Make_Date = models.DateField( )
    Price = models.IntegerField( )
class Car_InventoryAdmin(admin.ModelAdmin):
    list_display = ('No_Plate', 'Car_Model', 'Car_Type', 'Mileage', 'Engine_Type','Make_Date', 'Price')