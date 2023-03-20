from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse

# Create your views here.


def home(request):
    form = StudentRegistration()
    student = User.objects.all()
    return render (request, 'myapp/home.html', {'form':form, 'student':student})

def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            city = request.POST['city']
            usr = User(name=name, email=email, password=password, city=city)
            usr.save()
            return JsonResponse ({'status':'save'})
        print(form.errors)
        return JsonResponse ({'status':0})  