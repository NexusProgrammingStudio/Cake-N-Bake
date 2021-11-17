from django.db import models
import datetime

Default_Option = "'Please Select a Option'"

# Create your models here.
cake = {(Default_Option, Default_Option), ('Eggless', 'Eggless'), ('Egg', 'Egg')}
weight = {(Default_Option, Default_Option), ('500gms', '500gms'), ('1kg', '1kg'), ('2kg', '2kg')}
Category = {('Cake', 'Cake'), ('Chocolate', 'Chocolate'), ('Gift', 'Gift')}


class Cart(models.Model):
    Product_Name = models.ForeignKey('Cataloge.Product', on_delete=models.CASCADE)
    C_P_ID = models.IntegerField(default='100')
    Qty = models.PositiveIntegerField(default='1')
    Price = models.IntegerField(default='0')
    T_Price = models.IntegerField(default='0')
    fkuser = models.CharField(max_length=80, null=True, blank=True, default='Final_Master')
    Egg_or_Eggless = models.CharField(("Type_of_Cake"), max_length=60, choices=cake, default=Default_Option,
                                      blank=False, null=False)
    Weight = models.CharField(max_length=60, choices=weight, default=Default_Option, blank=False, null=False)

    def __str__(self):
        return str(self.Product_Name)


class Order(models.Model):
    Product_Name = models.ForeignKey('Cataloge.Product', on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField(default='1')
    Price = models.IntegerField(default='0')
    T_Price = models.IntegerField(default='0')
    fkuser = models.CharField(max_length=80, null=False, blank=True, default='Final_Master')
    Mark = models.CharField(max_length=20, null=False, blank=False, default="C'n'B")
    Order_id = models.IntegerField(blank=False, null=True)
    Date_of_Purchase = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return str(self.Product_Name) if self.Product_Name else ''


class Wishlist(models.Model):
    Product_Name = models.ForeignKey('Cataloge.Product', on_delete=models.CASCADE)
    W_P_ID = models.IntegerField(default='100')
    Price = models.IntegerField(default='0')
    fkuser = models.CharField(max_length=80, null=True, blank=True, default='Final_Master')
    Egg_or_Eggless = models.CharField(max_length=60, choices=cake, default=Default_Option, blank=True, null=True)
    Weight = models.CharField(max_length=60, choices=weight, default=Default_Option, blank=True, null=True)

    def __str__(self):
        return str(self.Product_Name)


class Checkout(models.Model):
    fkuser = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    contact_no = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    Address = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.first_name
