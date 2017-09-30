from django.shortcuts import render
from .models import PurchaseInfo
from .forms import purchaseentry


# Create your views here.

def home(request):
    return render(request,'base.html',{})

def Purchase_Invoice(request):
    form = purchaseentry()
    if request.method == 'POST':
        form = purchaseentry(request.POST)
        if form.is_valid():
            form.save()        
    context = {'form':form,}
    return render(request,'purchaseinvoice.html',context)

def Purchase_Main(request):
	return render(request,'')