from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse('My first django program')
def course(request):
    return HttpResponse('This is course page')
def courseDetailsAsInt(request,course_id):
    return HttpResponse(f'This is {course_id} course page')
def courseDetailsAsString(request,course_name):
    return HttpResponse(f'This is {course_name} course page')
def courseDetailsAsSlug(request,course_slug):
    return HttpResponse(f'Course page slug is {course_slug}')
def masterPage(request):
    data = {
        'language' : 'Python',
        'name' : 'Subhankar'
    }
    return render(request,'master.html',data)

def EmpFetch(request):
    
    data = {
        'student_datils' :[
        {"name" : "Subhankar Dutta","age" : 27, "department": "Web Developer"},
        {"name" : "Saikat Mudi","age" : 25, "department": "Software Developer"},
        {"name" : "Avishek Halder","age" : 28, "department": "Seniour PHP Developer"},
        ],
    }
    return render(request,'allEmp.html',data)

def HomePage(request):
    return render(request,'index.html')

def AboutPage(request):
    return render(request,'about.html')

def ServicePage(request):
    return render(request,'service.html')

def TeamPage(request):
    return render(request,'team.html')

def ContactPage(request):
    return render(request,'contact.html')