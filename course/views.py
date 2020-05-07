from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Course,Student,course_enrolment

def index(request):
    return HttpResponse("this is courseIndex")

def coursedetails(request,course_id):

    ceList = course_enrolment.objects.filter(course = course_id)
    output = 'course name is ' + ceList[0].curse.name;
    if ceList.count()<=0:
        output = output + ' and no student enrolled for this course';
    else:
        output = output + ' and student enrolled for this course are ';
    for ce in ceList:
        output = output +'\n'+ce.student.name;


    return HttpResponse(output);

def studentdetails(request,student_id):

    ceList = course_enrolment.objects.filter(student = student_id)
    output = 'student  name is ' + ceList[0].student.name;
    if ceList.count() <= 0:
        output = output + ' and student is not enrolled for any course';
    else:
        output = output + ' and student enrolled for courses ';
    for ce in ceList:
        output = output +'\n'+ce.course.name;


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



