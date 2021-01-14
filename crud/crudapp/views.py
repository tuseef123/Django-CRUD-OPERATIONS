from django.shortcuts import render,redirect
from crudapp.models import record
from .forms import colform
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def records(request):
    if request.method=="POST":
        p_name=request.POST["p_name"]
        catagory=request.POST["catagory"]
        quantity=request.POST["quantity"]
        quality=request.POST["quality"]
        room=request.POST["room"]
        dataa=record(p_name=p_name,catagory=catagory,quantity=quantity,quality=quality,room=room)
        dataa.save()
        return redirect('index')
    else:
        return render(request,'record.html')
def show(request):
    data=record.objects.all()
    return render(request,'recordshow.html',{'data':data})

def update(request,pk):
    fetch_data= record.objects.get(pk=pk)
    form = colform(instance=fetch_data)
    if request.method == 'POST':
        form = colform(request.POST,instance=fetch_data)
        if form.is_valid():
            form.save()
            # return redirect('show')
            messages.add_message(request,messages.SUCCESS,'Data has been updated Successfully!')
        # print(data_fetch)
    return render(request,'edit.html',{'data':fetch_data})

def delete(request,id):
    data=record.objects.get(id=id)
    data.delete()
    return redirect('show')