from django.db import models

# Create your models here.
class Dealer(models.Model):
    dealer_name = models.CharField(max_length=20)
    dealer_email = models.EmailField(max_length=20)
    dealer_number = models.CharField(max_length=15)
    dealer_address = models.TextField(max_length=70)

    def __str__(self):
        return f"{self.dealer_name}"

class Medicine(models.Model):
    medicine_code = models.IntegerField(unique=True)
    medicine_name = models.CharField(max_length=20)
    medicine_dealer_name = models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='medicines')
    medicine_price = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_stock = models.PositiveIntegerField()
    medicine_desc = models.TextField()

    class Meta:
        ordering = ['medicine_code']

    def __str__(self):
        return self.medicine_name


class Employee(models.Model):
    employee_id = models.IntegerField(unique=True)
    employee_first_name = models.CharField(max_length=20)
    employee_last_name = models.CharField(max_length=20)
    employee_address = models.CharField(max_length=20)
    employee_salary = models.IntegerField()
    employee_contact = models.IntegerField()
    employee_email = models.EmailField()

    class Meta:
        ordering = ['employee_id']

    def __str__(self):
        return f"{self.employee_first_name},{self.employee_last_name}"
    

class Customer(models.Model):
    customer_first_name = models.CharField(max_length=20)
    customer_last_name = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=20)
    customer_contact = models.IntegerField()
    customer_email = models.EmailField()

    class Meta:
        ordering = ['customer_first_name']

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name}"

class Purchase(models.Model):
    product_name = models.CharField(max_length=20)
    purchase_customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE)
    purchase_contact = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['product_name']


    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name}"
