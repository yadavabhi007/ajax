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
            sid = request.POST['stuid']
            name = request.POST['name']
            email = request.POST['email']
            city = request.POST['city']
            if sid:
                usr = User(id=sid, name=name, email=email, city=city)
            else:
                usr = User(name=name, email=email, city=city)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse ({'status':'Save', 'student_data':student_data})
        print(form.errors)
        return JsonResponse ({'status':'Not Save'}) 
    

def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        User.objects.get(id=id).delete()
        return JsonResponse ({'status':1}) 
    return JsonResponse ({'status':0})


def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        student = User.objects.get(id=id)
        student_data = {'id':student.id, 'name':student.name, 'email':student.email, 'city':student.city}
        return JsonResponse (student_data)
    

