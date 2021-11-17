from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

Default_Option = "'Please Select a Option'"

cake = {(Default_Option, Default_Option), ('Eggless', 'Eggless'), ('Egg', 'Egg')}
weight = {(Default_Option, Default_Option), ('500gms', '500gms'), ('1kg', '1kg'), ('2kg', '2kg')}
Category = {('Cake', 'Cake'), ('Chocolate', 'Chocolate'), ('Gift', 'Gift')}
Relation = {('Parents', 'Parents'), ('Siblings', 'Siblings'), ('Kids', 'Kids'), ('Girlfriend', 'Girlfriend'),
            ('Boyfriend', 'Boyfriend')}
Occasion = {('Birthday', 'Birthday'), ('Anniversary', 'Anniversary'), ('Weddings', 'Weddings')}


class Product(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    P_ID = models.IntegerField(default='100')
    Category = models.CharField(max_length=500, choices=Category)
    Relation = MultiSelectField(max_length=500, choices=Relation)
    Occasion = MultiSelectField(max_length=500, choices=Occasion)
    Name = models.CharField(max_length=500)
    Price_500gms = models.IntegerField(default='0')
    Price_1kg = models.IntegerField(default='0')
    Price_2kg = models.IntegerField(default='0')
    Price_Other_Products = models.IntegerField(default='0')
    Pic = models.ImageField(upload_to='Product', blank=False, null=False)
    desc = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.Name


class Cart_Cateloge(models.Model):
    Product_Name = models.ForeignKey(Product, on_delete=models.CASCADE)
    Qty = models.PositiveIntegerField(default='1')
    Price = models.IntegerField(default='0')
    T_Price = models.IntegerField(default='0')
    fkuser = models.CharField(max_length=80, null=True, blank=True)
    Egg_or_Eggless = models.CharField(max_length=60, choices=cake, default=Default_Option, blank=False, null=False)
    Weight = models.CharField(max_length=60, choices=weight, default=Default_Option, blank=False, null=False)

    def __str__(self):
        return self.Product_Name


class Wishlist_Cateloge(models.Model):
    Product_Name = models.ForeignKey(Product, on_delete=models.CASCADE)
    cid = models.IntegerField(default='0')
    Price = models.IntegerField(default='0')
    fkuser = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.Product_Name
