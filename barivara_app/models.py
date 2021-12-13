from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
import datetime
class owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone =  models.CharField(max_length=200)
    email =  models.EmailField(max_length=200,null=True)
    address =  models.CharField(max_length=500)
    occupation = models.CharField(max_length=100)
    nation_id = models.CharField(max_length=100)
    referal_id = models.CharField(max_length=200,default='default')
    password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class renter(models.Model):
    renter_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    birth_date = models.DateField(auto_now=False,auto_now_add=False)
    permanent_address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=100)
    phone =  models.CharField(max_length=200)
    email =  models.EmailField(max_length=200,null=True)
    nation_id = models.CharField(max_length=100)
    emergancy_name = models.CharField(max_length=200)
    emergancy_phone = models.CharField(max_length=200)
    # rented_flat_number = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



class flat_details(models.Model):
    flat_id = models.AutoField(primary_key=True)
    flat_owner_id = models.ForeignKey(owner,on_delete=CASCADE)
    flat_renter_id = models.ForeignKey(renter,on_delete=CASCADE,default=None)
    rent_amount = models.FloatField()
    size = models.CharField(max_length=100)
    flat_number = models.CharField(max_length=50)
    flat_floor_number = models.CharField(max_length=10)
    flat_description = models.CharField(max_length=1000,default='')
    flat_address = models.CharField(max_length=200,default='')




class earning(models.Model):
    earning_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(owner,on_delete=CASCADE)
    renter_id = models.ForeignKey(renter,on_delete=RESTRICT)
    flat_id = models.ForeignKey(flat_details,on_delete=CASCADE)
    earning_month = models.CharField(max_length=10,null=True)
    earning_date = models.DateField(auto_now=False,auto_now_add=False)
    rent_of_month_year = models.CharField(max_length=100)
    earned_amount = models.FloatField()




class remain(models.Model):
    remaining_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(owner,on_delete=CASCADE)
    renter_id = models.ForeignKey(renter,on_delete=RESTRICT)
    flat_id = models.ForeignKey(flat_details,on_delete=CASCADE)
    earning_id = models.ForeignKey(earning,on_delete=CASCADE,default=1)
    date = models.DateField(auto_now=False,auto_now_add=False,default=datetime.datetime.now)
    remain_month = models.CharField(max_length=10,null=True)
    remained_amount = models.FloatField()
    notes = models.TextField(max_length=500)

    def get_year(self):
        return self.date.year

