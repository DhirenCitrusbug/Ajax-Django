from django.http import JsonResponse
from django.shortcuts import render
from crud.models import User
from crud.form import StudentRegistration
# Create your views here.
def index(request):
    form = StudentRegistration()
    students = User.objects.all()
    context = {'form':form,'students':students}
    return render(request,'index.html',context)

def save_data(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print('fdfd',id)

        if id != None:
            user = User.objects.get(id=id)
            user.name = name
            user.email = email
            user.password = password
            user.save()
        else:
            print(id,'dfsfdsd')
            # user = User.objects.create(name=name,email=email,password=password)
            # user.save()

        student_data = User.objects.values()
        student_data = list(student_data)


        return JsonResponse({'status':'saved','student_data':student_data})
    return JsonResponse({'status':0})


def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        std = User.objects.get(id=id)
        std.delete()
        return JsonResponse({'status':'deleted'})

def edit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        std = User.objects.get(id=id)
        student_data = {'id':std.id,'name':std.name,'email':std.email,'password':std.password}
        return JsonResponse({'status':'saved','student_data':student_data})