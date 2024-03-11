from django.db import models

# Create your models here.

class Items(models.Model):
  name=models.CharField(max_length=50)
  def __str__(self):
       return self.name

class ItemDetails(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    img=models.CharField(max_length=50,null=True)
    tax=models.FloatField()
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemmsid=models.ForeignKey(Items,on_delete=models.CASCADE,null=True)
    def __str__(self):
       return self.price
  


class Carrt(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)



class Itemsipad(models.Model):
  name=models.CharField(max_length=50)
  def __str__(self):
       return self.name

class ItemDetailsipad(models.Model):
    color=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    img=models.CharField(max_length=50,null=True)
    tax=models.FloatField()
    total=models.FloatField()
    date=models.DateTimeField(auto_now_add=True)
    itemmsid=models.ForeignKey(Itemsipad,on_delete=models.CASCADE,null=True)
    def __str__(self):
       return self.price


class Carrt_ipad(models.Model):
    Id_product=models.IntegerField()
    Id_user=models.IntegerField()
    price=models.FloatField()
    qty=models.IntegerField()
    tax=models.FloatField()
    total=models.FloatField()
    discount=models.FloatField()
    net=models.FloatField()
    status=models.BooleanField()
    Created_at=models.DateTimeField(auto_now_add=True)

class Paynoww(models.Model):
    Id_user=models.IntegerField()
    name_in_card=models.CharField(max_length=50)
    number_card=models.IntegerField()
    date_card=models.CharField(max_length=50)
    cvv_card=models.IntegerField()
    date_add=models.DateTimeField(auto_now_add=True)
    
class Payno(models.Model):
    name_in_card=models.CharField(max_length=50)
    number_card=models.IntegerField()
    date_card=models.CharField(max_length=50)
    cvv_card=models.IntegerField()
    date_add=models.DateTimeField(auto_now_add=True)
    
    
    




