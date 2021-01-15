from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Profile
from .forms import AddData
# Create your views here.
def home(request):
    profile = Profile.objects.all()
    if request.method =='POST':
        form = AddData(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Record Added Successfully')
            return redirect('home')

    else:
        form = AddData()
    return render(request,'message_show/home.html',{'profiles':profile,'form':form})

def edit(request,pk):
    data_fetch = Profile.objects.get(pk=pk)
    form = AddData(instance = data_fetch)
    if request.method =='POST':
        form = AddData(request.POST,instance = data_fetch)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Record updated Successfully')
            return redirect('home')
    return render(request,'message_show/edit.html',{'form':form})


def delete(request,pk):
    data = Profile.objects.get(pk=pk)
    data.delete()
    messages.add_message(request,messages.SUCCESS,'Record Deleted Successfully')
    return redirect('home')