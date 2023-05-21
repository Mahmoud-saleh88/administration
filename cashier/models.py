from django.db import models
from django.utils import timezone


class MenuItem(models.Model):
    itemID = models.AutoField(primary_key=True, db_column="itemID")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    itemphoto =  models.ImageField(upload_to='media/', null= True)
    photouploaded_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Order(models.Model):
    #menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    # quantity = models.PositiveIntegerField(default=1)
    date = models.DateField(default=timezone.now, db_column="Creation_date")
    time = models.TimeField(default=timezone.now, db_column="Creation_time")
    cashier_name = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem,related_name="Items")
    totalprice = models.PositiveIntegerField(db_column="totalprice", default=0.0)
    
    def __str__(self):
        return f"Order ID: {self.id}"


class Order_Items(models.Model):
    order_items_id = models.AutoField(primary_key=True,db_column="Order_Items_ID")
    menu_item = models.ForeignKey(MenuItem,related_name="MenuItems",blank=True,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(Order,related_name="Order_Item",on_delete=models.CASCADE)