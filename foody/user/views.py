from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Account
from .forms import RegistrationForms
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect 

# Create your views here.
def home(request):
    return render(request,'index.html')

# @csrf_exempt  

@csrf_protect
def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')   
    form=RegistrationForms
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            request.session['first_name']=first_name
            last_name = form.cleaned_data['last_name']
            request.session['last_name']=last_name
            phone_number= form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            request.session['email']=email
            password = form.cleaned_data['password']
            request.session['password']=password
            username =str(first_name+last_name)
            request.session['username']=username
            request.session['phone_number']=phone_number


            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number = phone_number
            user.save()

    return render(request,'demo.html')