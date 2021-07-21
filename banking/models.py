from django.db import models

# Create your models here.
    
class banker(models.Model):
    name = models.CharField(max_length=50,default="")
    email=models.EmailField(max_length=50)
    amt=models.IntegerField(default=0)
    userid= models.IntegerField(default=0)

    def __str__(self):
        return self.name   

class History(models.Model):
    source_name = models.CharField(max_length=122)
    sender_acc_no = models.CharField(max_length=122)
    Current_balance = models.IntegerField()
    money_deposit = models.IntegerField()
    receiver_name = models.CharField(max_length=122)
    date = models.DateField()
     
    