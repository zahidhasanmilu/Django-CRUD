from django.http import HttpResponse
from django.shortcuts import redirect, render

import studentsinfo
from .forms import StudentForm
from .models import Student

# Create your views here.
def allstudent(request):
    files = Student.objects.all()
    if request.method == "GET":
        file = request.GET.get('search_file')
        if file != None:
            files = Student.objects.filter(name__icontains=file)
    return render(request, 'index.html', {'files':files})



def addstudent(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm =StudentForm()
    return render(request, 'addstudentform.html', context={'forms':fm})


def update(request,id):
    file = Student.objects.get(id=id)    
    if request.method == 'POST':        
        form = StudentForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=StudentForm(instance=file)
    return render(request, 'update.html', {'form':form})


def delete_student(request,id):
    if request.method =='POST':
        files = Student.objects.get(id=id)
        files.delete()
        return HttpResponse('Delete Student')
    
