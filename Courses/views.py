from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def home(request):
    return render(request, 'home.html')

def spes(request):
    if request.method == 'POST':
        Speciality.objects.create(
            name = request.POST['nom'],
            code = request.POST['code'],
            start_date = request.POST['start'],
            is_active = True
        )
        return redirect('/Yonalish/')

    specials = Speciality.objects.all()
    return render(request, 'special.html', {'Specials' : specials})

def ustozlar(request):
    if request.method == 'POST':
        Teacher.objects.create(
            first_name = request.POST['nom'],
            last_name = request.POST['fam'],
            degree = request.POST['daraja']
        )
        return redirect('/ustozlar/')

    Ustozlar = Teacher.objects.all()
    return render(request, 'Ustozlar.html', {'Ustozlar' : Ustozlar})

def ustoz_ochir(request, pk):
    Teacher.objects.get(id = pk).delete()
    return redirect('/ustozlar/')

def spes_ochir(request, son):
    Speciality.objects.get(id = son).delete()
    return redirect('/Yonalish/')

def fanlar(request):
    Subjects = Subject.objects.all()
    return render(request, 'fanlar.html', {'Subjects' : Subjects})