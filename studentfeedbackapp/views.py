from django.shortcuts import render
from django.http import HttpResponse
from studentfeedbackapp.models import  student,feedback_oncourse,feedback_onfaculty
# Create your views here.
from sqlalchemy.testing.provision import register
def stdhome(request):
    return render(request,'studentlogin.html')
def stdreg(request):
    return render(request,'studentregister.html')
def writestudent(request):
    name = request.GET['regname']
    number = request.GET['mob']
    passw = request.GET['pass']
    cpass = request.GET['cpass']
    if len(name) == 0 or len(number) == 0 or len(passw) == 0 or len(cpass) == 0 or passw != cpass or len(number) < 10:
        txt = "NOT VALID"
    else:
        value = student(name=name, number=number, password=passw)
        value.save()
        txt = "SUCCESSFULLY REGISTERED LOGIN"
    return render(request, 'studentregister.html', {"txt": txt})
def slogin(request):

    number = request.GET['num']
    password = request.GET['password']
    if len(number) == 0 or len(password) == 0:
        txt = "FILL THE FIELDS"
        return render(request, 'studentlogin.html', {"txt": txt})
    else:
        data = student.objects.filter(number=number, password=password).values()
        if len(data) == 0:
            txt = "invalid number/password"
            return render(request, 'studentlogin.html', {"txt": txt})
        else:
            # [{'id': 1, 'name': 'praveen kumar', 'number': 8714249383,   'password': 'password'}]
            global num
            num = data[0]["number"]
            print("/////////////////////////////////////////////////////", number)
            return render(request, 'selection.html')


def s_cource_feedb(request):
    return render(request,"s_course.html")

def up_st_fee_co(request):

    global num

    department=request.GET['department']
    sem=request.GET['sem']
    content=request.GET['content']
    coverage=request.GET['coverage']
    application=request.GET['application']
    value=request.GET['value']
    clarity=request.GET['clarity']
    metirial=request.GET['metirial']
    effort=request.GET['effort']
    overall=request.GET.get('overall')

    #print(department,sem,content,coverage,application,value,clarity,metirial,effort,overall)
    value=feedback_oncourse(number=num,department=department,sem=sem,content=content,coverage=coverage,application=application,value=value,
                            clarity=clarity,metirial=metirial,effort=effort,overall=overall)
    value.save()



    return HttpResponse("SUBMITTED")


def s_faculty_feedb(request):
    return render(request,"s_faculty_feedb.html")


#this make sens evde





def up_st_fee_faculty(request):

    global num
    department=request.GET['department']

    sem=request.GET['sem']
    teacher = request.GET['teacher']
    knowledge=request.GET['knowledge']
    communication=request.GET['communication']
    Commitment=request.GET['Commitment']
    interest=request.GET['interest']
    integratingskill=request.GET['integratingskill']
    integratecontent=request.GET['integratecontent']
    accessibility=request.GET['accessibility']
    cordination=request.GET['cordination']
    provision=request.GET['provision']
    overall=request.GET['overall']

    #print(department,sem,teacher,knowledge,communication,Commitment,interest,integratingskill,integratecontent,accessibility,cordination,provision,overall)
    value=feedback_onfaculty(number=num,department=department,sem=sem,teacher=teacher,knowledge=knowledge,communication=communication,Commitment=Commitment,
                             interest=interest,integratingskill=integratingskill,integratecontent=integratecontent,
                             accessibility=accessibility,cordination=cordination,provision=provision,overall=overall)


    value.save()

    return HttpResponse("UPLOADED")


def stdactivity(request):

    global num
    cdata=feedback_oncourse.objects.filter(number=num).values()
    if len(cdata)==0:
        ctxt="NO ACTIVITIES FOUND"

    else:
        licource=[]
        for i in range(len(cdata)):

             licource.append("You reviewed on :"+cdata[0]['department']+" :department")


    cdata=feedback_onfaculty.objects.filter(number=num).values()
    if len(cdata)==0:
        ctxt="NO ACTIVITIES FOUND"

    else:
        lifaculty=[]
        for i in range(len(cdata)):

             licource.append("You reviewed on Mr/Ms:"+cdata[0]['teacher'])

    if len(licource)==0 and  len(lifaculty)==0:
        return HttpResponse("NO ACTIVITIES")
    else:
        return render(request,"all.html",{'data':licource,'fac':lifaculty})
