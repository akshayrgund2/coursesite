from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import StudentForm, EnrollForm
from django.db import connection

import json

# Create your views here.

from django.http import HttpResponse
from .models import Course,Student,course_enrolment
from django.template import loader

def index(request):
    studentlist = Student.objects.all()
    studentdict = {};
    allstudentdict = {};
    for s in studentlist:
        studentdict['email'] = s.email
        studentdict['rollnumber'] = s.rollnumber
        studentdict['phone'] = s.phone
        allstudentdict['student '+ s.name] = studentdict;

    return HttpResponse(json.dumps(allstudentdict))



def coursedetails(request,course_id):

    ceList = course_enrolment.objects.filter(course = course_id)
    course = ceList[0].course;
    templet  = loader.get_template('course/index.html')
    context = {
       'course' : course,
        'ceList' : ceList,
    }

    return HttpResponse(templet.render(context,request)) ;




def studentdetails(request,student_id):
    #ceList = course_enrolment.objects.filter(student = student_id)
    details = {};
    details["name"] = Student.objects.raw('SELECT * FROM course_student')[0].name

    with connection.cursor() as cursor:
        cursor.execute(
            "select * from course_course "
            "join course_course_enrolment on course_course.id = course_course_enrolment.course_id "
            "where course_course_enrolment.student_id = %s",[student_id]
        )
        details['courses'] = cursor.fetchall()


    return HttpResponse(json.dumps(details));



@login_required(login_url='/accounts/login/')
def enrollform(request):
    context = {}
    form = EnrollForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form;
    return render(request, 'course/enroll.html', context)


@login_required(login_url='/accounts/login/')
def enroll(request):
    c = Course(request.POST['course'])
    s = Student(request.POST['student'])
    ce = course_enrolment(course = c,student = s)
    ce.save();
    return HttpResponse('Enrolled')

@login_required(login_url='/accounts/login/')
def addcourseform(request):
    context = {}
    return render(request, 'course/addcourse.html', context)

@login_required(login_url='/accounts/login/')
def addcourse(request):

    courses = Course.objects.filter(name = request.POST['coursename'])
    if courses.count()>0:
        return HttpResponse("course already present");
    c = Course();
    c.name = request.POST['coursename'];
    c.fees = request.POST['fees'];
    c.institute = request.POST['institute'];
    c.save();
    return HttpResponse("course is added")


@login_required(login_url='/accounts/login/')
def addstudentform(request):
    context = {}
    form = StudentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form'] = form
    return render(request, 'course/addstudent.html', context)


@login_required(login_url='/accounts/login/')
def addstudent(request):

    s = Student();
    s.name = request.POST['name']
    s.email = request.POST['email']
    s.phone = request.POST['phone']
    s.rollnumber = request.POST['rollnumber']
    s.save()
    return HttpResponse('student added')

def updatecoursename(request,course_id,name):
    courses = Course.objects.filter(id=course_id)
    if courses.count() <= 0:
        return HttpResponse("course not  present");
    c = courses[0];
    c.name = name;
    c.save()
    return HttpResponse('Course name is updated')

def updatestudentname(request,student_id,name):
    students = Student.objects.filter(id=student_id)
    if students.count() <= 0:
        return HttpResponse("student not  present");
    c = students[0];
    c.name = name;
    c.save()
    return HttpResponse('student name is updated')

def deletestudent(request,student_id):
    students = Student.objects.filter(id = student_id)
    if students.count()<=0 :
        return HttpResponse("student not found")
    s = students[0];
    s.delete()
    return HttpResponse("student is deleted")

def deletecourse(request,course_id):
    courses = Course.objects.filter(id = course_id)
    if courses.count()<=0 :
        return HttpResponse("course not found")
    s = courses[0];
    s.delete()
    return HttpResponse("courses is deleted")



