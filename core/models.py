from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class HSN(models.Model):
	HSN = models.IntegerField(null = True)

class GSTkey(models.Model):
	gstrate = models.IntegerField(null = True)
 
#  Need to give more validators for Gstin , serial no
class PurchaseInfo(models.Model):
	SerialNumber = models.CharField(max_length=20,blank=True,null= True, validators=[RegexValidator(r'^[0-9]{2}[a-zA-Z]*$',message= 'Only alphanumeric characters are allowed.')])
	Duedate = models.DateField("Time which date of bill going to be invalid",null=True)
	Refernce = models.CharField(max_length=30,null=True,default='Null')
	VendorName = models.CharField(max_length=50)
	ItemDescription = models.TextField()
	GSTIN = models.CharField(max_length=15,blank=True, validators=[RegexValidator(r'^[0-9]{2}[a-zA-Z]{11}[0-9]*$',message= 'Enter valid GSTIN no')])
	type=(
		('S','Services'),
		('G','Goods'),
		)
	date = models.DateField(" Invoice was made on:",null=True)
	ItemType = models.CharField(max_length=30,choices=type,default='SOME STRING')
	HSNa = models.ForeignKey(HSN, on_delete=models.CASCADE,null=True)
	Qty = models.IntegerField(null=True)
	Units = models.IntegerField(null=True)
	Rate = models.ForeignKey(GSTkey,on_delete=models.CASCADE,null=True)
	Discount = models.IntegerField(null=True)
	Taxable_value = models.IntegerField(null=True)
	CGST = models.IntegerField(null=True)
	SGST = models.IntegerField(null=True)

	def __str__(self):
		return self.SerialNumber
