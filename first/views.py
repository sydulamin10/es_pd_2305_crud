from django.shortcuts import render, redirect
from .models import Human
from django.db.models import Q
import os


def first_func(request):
    all_data = Human.objects.all()
    if request.method == 'POST':
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        image = request.FILES.get('img')
        if Human.objects.filter(name=name).exists():
            massage = 'Already Data Exist'
        else:
            human = Human.objects.create(name=name, age=age, image=image)
            human.save()
            massage = 'Data Added'

    if request.method == 'GET':
        src = request.GET.get('src')
        if src:
            all_data = Human.objects.filter(name__icontains=src)

    return render(request, 'new.html', locals())


def delete_data(request, id):
    data = Human.objects.get(id=id)
    if data.image != 'def.png':
        os.remove(data.image.path)
    data.delete()
    return redirect('/')


def update_data(request, id):
    data = Human.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('Name')
        age = request.POST.get('Age')
        image = request.FILES.get('img')
        if Human.objects.filter(Q(name=name) | Q(age=age)).exists():
            massage = 'Already Data Exist'
        else:
            data.name = name
            data.age = age
            if data.image != 'def.png':
                os.remove(data.image.path)
                data.image = image
            data.save()
            massage = 'Data Updated'
            return redirect('/')
    return render(request, 'update.html', locals())
