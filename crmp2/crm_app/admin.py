from django.contrib import admin
from .models import Customer, Product, Employee, Task
from django.contrib.admin import DateFieldListFilter

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'stock')
    search_fields = ('name', 'price')
    list_filter = ('stock','description')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position')
    search_fields = ('name', 'email')
    list_filter = ('position',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'created_at', 'description')
    search_fields = ('title', 'assigned_to__name', 'description')
    list_filter = ('status',  ('created_at', DateFieldListFilter))
