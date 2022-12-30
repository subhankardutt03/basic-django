from django.http import HttpResponse,HttpResponseRedirect
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
    # if request.method == 'GET':
    #     output = request.GET.get('output')
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            
            data = {
                'name':name,
                'email':email,
                'phone':phone
            }
    except:
        pass
    return render(request,'index.html',data)

def AboutPage(request):
    return render(request,'about.html')

def ServicePage(request):
    return render(request,'service.html')

def TeamPage(request):
    return render(request,'team.html')

def ContactPage(request):
    data={}
    try:
        # name = request.GET.get('name')
        # email = request.GET.get('email')
        # phone = request.GET.get('phone')
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            data = {
                'name': name,
                'email': email,
                'phone': phone 
            }
            # allData = f"{name}|{email}|{phone}"
            # url = '/?output={}'.format(allData)
            # return HttpResponseRedirect(url)
    except:
        pass
    return render(request,'contact.html',data)