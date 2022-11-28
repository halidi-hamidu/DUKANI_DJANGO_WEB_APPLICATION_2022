from datetime import datetime
from itertools import product
from django.db import models
import uuid
from django.contrib.auth.models import User
from twilio.rest import Client
import os

# Create your models here.


class ProductTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=100)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products List'

    def __str__(self):
        return str(self.product_name)


class ProductAndSupplierTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    supplier_full_name = models.CharField(max_length=100)
    supplier_phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    product_name = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'suppliers products List'

    def __str__(self):
        return str(self.supplier_full_name)


# EmployeeDetailInformations
class EmployeeDetailInformations(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    employee_Full_name = models.CharField(max_length=200)
    employee_gender = models.CharField(max_length=100)
    employee_email_address = models.EmailField()
    employee_start_date = models.DateField(auto_now_add=True)
    employee_phone_number1 = models.CharField(max_length=100)
    employee_phone_number2 = models.CharField(max_length=100)
    employee_residence_area = models.CharField(max_length=100)
    employee_username = models.CharField(max_length=100, null=True, blank=True)
    employee_password = models.CharField(max_length=100, null=True, blank=True)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'list of Employees'

    def __str__(self):
        return str(self.employee_Full_name)

# ShopsTable


class ShopsTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    shop_name = models.CharField(max_length=100)
    shop_street = models.CharField(max_length=100)
    shop_district = models.CharField(max_length=100)
    shop_region = models.CharField(max_length=100)
    shop_start_date = models.DateTimeField(auto_now_add=True)
    shop_supervisor = models.ForeignKey(
        EmployeeDetailInformations, on_delete=models.CASCADE)
#   created_at = models.DateTimeField(auto_now_add =True) #never change once the object is created
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Shops List'

    def __str__(self):
        return str(self.shop_name)

# ProductAndSupplierAndReceiverTable


class ProductAndSupplierAndReceiverTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    product_cost = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    product_quantity = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    total_product_cost = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    amount_to_sold = models.PositiveIntegerField(null=True, blank=True)
    supplier_full_name = models.ForeignKey(
        ProductAndSupplierTable, on_delete=models.CASCADE)
    shop_info = models.ForeignKey(ShopsTable, on_delete=models.CASCADE)
    product_receiver = models.ForeignKey(
        EmployeeDetailInformations, on_delete=models.CASCADE)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products received '

    def __str__(self):
        return str(self.product_name)

# productSoldInCash


class productSoldInCash(models.Model):
    now_date = datetime.today().date()
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.ForeignKey(
        ProductAndSupplierAndReceiverTable, on_delete=models.SET_NULL, null=True)
    number_of_product_nedeed = models.IntegerField()
    date_product_sold = models.DateTimeField(default=now_date)
    total_product_cost = models.PositiveIntegerField(null=True, blank=True)
    supervisor = models.ForeignKey(
        EmployeeDetailInformations, on_delete=models.SET_NULL, null=True)
    shop_name = models.ForeignKey(ShopsTable, on_delete=models.CASCADE)
    store_remain = models.PositiveIntegerField(null=True, blank=True)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products sold'

    def __str__(self):
        return str(self.product_name)


# EmergenceInformations
class EmergenceInformations(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    what_emergence = models.CharField(max_length=2000)
    spending_cost = models.IntegerField()
    spending_date = models.DateField()
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of emergence'

    def __str__(self):
        return str(self.what_emergence)


class CustomersOrders(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_Full_name = models.CharField(max_length=2000)
    customer_phone_number = models.IntegerField()
    customer_order = models.CharField(max_length=2000)
    customer_quantity_nedeed = models.IntegerField()
    delivery_date_expected = models.DateField()
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=300, default="Pending")
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of Orders from customers'

    def __str__(self):
        return str(self.customer_Full_name)


class AuthorizeUsers(models.Model):
    select_user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_dashboard = models.BooleanField(default=False)
    manage_employees = models.BooleanField(default=False)
    manage_shop = models.BooleanField(default=False)
    manage_product = models.BooleanField(default=False)
    manage_supplier = models.BooleanField(default=False)
    manage_store = models.BooleanField(default=False)
    manage_sales = models.BooleanField(default=True)
    manage_orders = models.BooleanField(default=True)
    manage_emergence = models.BooleanField(default=True)
    help_center = models.BooleanField(default=True)
    manage_company_stock_or_assets = models.BooleanField(default=False)
    manage_authorizations = models.BooleanField(default=False)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Authorization'

    def __str__(self):
        return str(self.select_user)

# CompanyStockOrAssets


class CompanyStockOrAssets(models.Model):
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    stock_number = models.CharField(max_length=100, blank=True, null=True)
    stock_color = models.CharField(max_length=100, null=True, blank=True)
    stock_size = models.CharField(max_length=100, null=True, blank=True)
    stock_image = models.ImageField(upload_to='media')
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Company Stock Or Assets'

    def __str__(self):
        return str(self.stock_name)
