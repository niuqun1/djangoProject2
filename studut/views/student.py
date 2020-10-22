from django.shortcuts import render,redirect
from studut.models import studet
from  studut.models import Clesses
def get_student(request):
    data=studet.objects.all()
    return render(request,'get_student.html',{'data':data})
def add_student(request):
    if request.method=='POST':

        name=request.POST.get('username')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        cless=request.POST.get('cs')
        studet.objects.create(username=name,age=age,sex=sex,cs_id=cless)
        return redirect('/get_student')
    elif request.method=='GET':
        clesses_data = Clesses.objects.all()
        return render(request,'add_student.html' ,{'cles':clesses_data})
def del_student(request):
    student_id=request.GET.get('nid')
    studet.objects.filter(id=student_id).delete()
    return redirect('/get_student')
def updata_student(request):
    if request.method=='GET':
        nid = request.GET.get('nid')
        data=studet.objects.get(id=nid)
        classes_id=request.GET.get(('classes_id'))
        classes=Clesses.objects.get(id=classes_id)
        classes_data=Clesses.objects.all()
        return render(request,'updata_student_Data.html',{'data':data,'classes':classes,'data_class':classes_data})
    elif request.method=='POST':
        name = request.POST.get('username')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        cless = request.POST.get('cs')
        studet.objects.filter(id=nid).update(username=name,age=age,sex=sex,cs_id=cless)
        return redirect('/get_student')


