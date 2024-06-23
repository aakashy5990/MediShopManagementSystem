from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Dealer)
class DealerModelAdmin(admin.ModelAdmin):
    list_display = ['id','dealer_name','dealer_email','dealer_number','dealer_address']

@admin.register(Medicine)
class MedicineModelAdmin(admin.ModelAdmin):
    list_display = ['medicine_code','medicine_name','medicine_dealer_name','medicine_price','medicine_stock','medicine_desc']

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['employee_id','employee_first_name','employee_last_name','employee_address','employee_salary','employee_contact','employee_email']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['customer_first_name','customer_last_name','customer_address','customer_contact','customer_email']

@admin.register(Purchase)
class PurchaseModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','purchase_customer_name','purchase_contact','purchase_price','purchase_quantity']