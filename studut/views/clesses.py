from django.shortcuts import render,redirect
from studut import models
def get_clesses(request):
    title=models.Clesses.objects.all()
    return  render(request,'get_clesses.html',{'title':title})
def add_classes_data(request):
    if request.method=="GET":
        return render(request,'add_classes_data.html')
    elif request.method=="POST":
        data=request.POST.get('title')
        models.Clesses.objects.create(title=data)
        return redirect('/classes')
def del_student_data(request):
        nid=request.GET.get('nid',123)
        models.Clesses.objects.filter(id=nid).delete()
        return redirect('/classes')
def updata_student_Data(request):
    if request.method == "GET":
        nid=request.GET.get('nid')
        data=models.Clesses.objects.get(id=nid)
        return render(request, 'updata_classes_data.html', {'data':data})
    elif request.method == "POST":
        data = request.POST.get('title')
        models.Clesses.objects.create(title=data)
        return redirect('/classes')

