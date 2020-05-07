from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Course,Student,course_enrolment

def index(request):
    return HttpResponse("this is courseIndex")

def totalstudents(request,course_id):

    ceList = course_enrolment.objects.filter(course = course_id)
    output = '';
    for ce in ceList:
        output = output +'\n'+ce.student.name;


    return HttpResponse(output);

def enroll(request,course_id,student_id):
    c = Course.objects.filter(id = course_id)[0];
    s = Student.objects.filter(id = student_id)[0];
    ce = course_enrolment(course = c,student = s)
    ce.save();
    return HttpResponse('Enrolled')

def addcourse(request,name):
    courses = Course.objects.filter(name=name)
    if courses.count()>0:
        return HttpResponse("course already present");
    c = Course(name = name);
    c.save();
    return HttpResponse("course is added")

def addstudent(request,name):

    c = Student(name = name);
    c.save();
    return HttpResponse("student is added")

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

