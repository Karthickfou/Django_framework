from django.db import models

class infant (models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    aadharno=models.CharField(max_length=200)
    panno=models.CharField(max_length=200)
    mobileno=models.CharField(max_length=200)
    accountno=models.CharField(max_length=200)
    
class gobi (models.Model):
     accountno=models.CharField(max_length=200)
     accountholder=models.CharField(max_length=200)
     balance=models.CharField(max_length=200)
     
       
    
    
    
