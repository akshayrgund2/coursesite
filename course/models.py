from django.db import models

# Create your models here.


from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)



class Student(models.Model):
    name = models.CharField(max_length=200)

class course_enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

