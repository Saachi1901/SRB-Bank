from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import banker,History
from django.db.models import F
from datetime import datetime


# Create your views here.

def history(request):
    
    if request.method =="POST":
        cust = request.POST.get('submit')
        query1 = banker.objects.get(name =cust)
        query2 = banker.objects.exclude(name = cust)
        receiver= request.POST.get('to')
        money = request.POST.get('amount2')
        sender = request.POST.get('submit')
        query2 = banker.objects.get(name = sender)
        query2.amt= F('amt')- money
        query2.save()
        query1 = banker.objects.get(name= receiver)
        query1.amt= F('amt')+ money
        query1.save()
        result = banker.objects.get(name = sender)
        transact = History()
        transact.source_name = sender
        transact.sender_acc_no = result.userid
        transact.Current_balance = result.amt
        transact.money_deposit = money
        transact.receiver_name = receiver
        transact.date = datetime.today()
        transact.save()
        return redirect('customers')
    all_entries = History.objects.all()
    print(all_entries)
    context = {
            "history" : all_entries
        }
    return render(request,'banking/history.html',context)


def home(request):
    return render(request,'banking/home.html')      

def customers(request):
    bankers=banker.objects.all()
    return render(request, 'banking/customers.html', {'bankers':bankers})
    

def next(request,mid):
    Banker= banker.objects.filter(id=mid)
    bankers=banker.objects.all()
    params = {'bankers':bankers,'Banker' :Banker[0]}
    return render(request,'banking/next.html',params)  
