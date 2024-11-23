from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1. models import Players

# Create your views here.
def CreatePlayers(request):
    if request.method=='POST':
        pname=request.POST['pname']
        age=request.POST['age']
        role=request.POST['role']
        nationality=request.POST['nationality']
        baseprice=request.POST['baseprice']
        Players.objects.create(pname=pname,age=age,role=role,nationality=nationality,baseprice=baseprice)
        # return HttpResponse("details stored")
        return redirect('display')
    return render(request,'index.html')

def display(request):
    qs=Players.objects.all()
    context={
        'players':qs
    }
    return render(request,'index1.html',context)

def update(request,id):
    new=Players.objects.filter(id=id)
    context={
        'player':new[0]
    }
    if request.method =='POST':
        pname=request.POST['pname']
        age=request.POST['age']
        role=request.POST['role']
        nationality=request.POST['nationality']
        baseprice=request.POST['baseprice']
        new.update(
            pname=pname,
            age=age,
            role=role,
            nationality=nationality,
            baseprice=baseprice
        )
        return redirect('display')
    return render(request,'index2.html',context)

def delete(request,id):
    erase=Players.objects.get(id=id)
    erase.delete()
    return redirect('display')
        

        

