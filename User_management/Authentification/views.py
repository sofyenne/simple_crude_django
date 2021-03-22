from .forms import UserCreate
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import ClientCreate

from django.http import HttpResponse

def index(request):
    context = {'listuser' : User.objects.all()}
    return render(request , 'list.html' , context)


def listsup(request):
    users = User.objects.all().filter(role='user')
    print(users)
    
    return render(request , 'listSup.html' , {'users' : users})




def upload(request):
    upload = UserCreate()
    if request.method == 'POST':
        upload = UserCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'register'}}">reload</a>""")
    else:
        return render(request, 'register.html', {'form':upload})

def addclient(request):
    form = ClientCreate()
    if request.method =='POST':
        form = ClientCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listsup')

        else:
            form = ClientCreate()
    else:
        return render(request , 'addclient.html', {'form' : form})            
        
        
         

def Login(request):
        if request.method== 'POST' :
                name = request.POST.get('name')
                password = request.POST.get('password')
                user =User.objects.filter(name=name).first()
                print(user)
                if user is not None and user.password==password :
                    if user.role=='superuser':
                        return redirect('index')  
                    if user.role=='admin':
                        return redirect('listsup') 
                    else:
                        return redirect('client')    
    
                else:
                    messages.info(request, 'username or password is incorrect')
        return render(request,'login.html') 
        
    

def delete(request , id )  :
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('index')


def indexclient(request):
    return render(request , 'indexclient.html')