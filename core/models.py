from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
 
#  Need to give more validators for Gstin , serial no
class PurchaseInfo(models.Model):
	SerialNumber = models.CharField(max_length=20,blank=True,null= True, validators=[RegexValidator(r'^[0-9a-zA-Z]*$',message= 'Only alphanumeric characters are allowed.')])
	Duedate = models.DateField(null=True)
	Refernce = models.CharField(max_length=30,null=True,default='Null')
	VendorName = models.CharField(max_length=50)
	ItemDescription = models.TextField()
	type=(
		('S','Services'),
		('G','Goods'),
		)
	ItemType = models.CharField(max_length=30,choices=type,default='SOME STRING')
	HSN = models.IntegerField()
	Qty = models.IntegerField(null=True)
	Units = models.IntegerField(null=True)
	Rate = models.IntegerField(null=True)
	Discount = models.IntegerField(null=True)
	Taxable_value = models.IntegerField(null=True)
	CGST = models.IntegerField(null=True)
	SGST = models.IntegerField(null=True)
	time = models.DateField(default = datetime.now())

	def __str__(self):
		return self.SerialNumber
