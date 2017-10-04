from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

def Purchase_DetailsView(request,id):
    data = PurchaseInfo.objects.get(pk=id)
    context = { 'data':data}
    return render(request,'purchase.html',context)

def Purchase_ListView(request):
    data_list = PurchaseInfo.objects.all()
    paginator = Paginator(data_list, 5)

    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data= paginator.page(paginator.num_pages)
    return render(request,'purchase_listview.html',{'data':data})

