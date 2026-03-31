# Ex01 Django ORM Web Application
## Date: 312/03/2026

## AIM
To develop a Django Application to store and retrieve data from an Online Food Delivery Database platform like Zomato or Swiggy using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
admins.py
~~~
from django.contrib import admin
from .models import Car_Inventory, Car_InventoryAdmin
admin.site.register(Car_Inventory, Car_InventoryAdmin)
~~~
models.py
~~~
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
~~~
## OUTPUT

![alt text](<Screenshot (26).png>)

## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
