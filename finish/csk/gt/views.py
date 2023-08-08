from django.shortcuts import render,redirect,HttpResponse
from . models import *

def index (request):
    if request.method=='POST':
        firstname=request.POST.get('firstname','')
        lastname=request.POST.get('lastname','')
        aadharno=request.POST.get('aadharno','')
        panno=request.POST.get('panno','')
        mobileno=request.POST.get('mobileno','')
        accountno=request.POST.get('accountno','')
        form=infant(firstname=firstname, lastname= lastname,aadharno=aadharno,panno=panno,mobileno=mobileno,accountno=accountno)
        form.save()
        return redirect(show)
    else:
        return render (request,'gt/first.html')
    
def show (request):
    if request.method=='POST':
        accountno=request.POST.get('accountno','')
        accountholder=request.POST.get('accountholder','')
        balance=request.POST.get('balance','')
        form=gobi( accountno= accountno,accountholder=accountholder,balance=balance)
        form.save()
        return HttpResponse("Hello world!")
    else:
        return render (request,'gt/second.html')
    
    
    
        
