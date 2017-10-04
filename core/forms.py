from django import forms

from .models import PurchaseInfo

class purchaseentry(forms.ModelForm):
	class Meta:
		model =  PurchaseInfo
		fields =['SerialNumber','Refernce','VendorName','ItemDescription','ItemType','HSNa','Qty','Units','Rate','Discount','Taxable_value','CGST','SGST']
