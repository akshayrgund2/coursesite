from django.db import models

# Create your models here.


from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    institute = models.CharField(max_length=200,null=True)
    fees = models.IntegerField(null=True)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    phone = models.BigIntegerField(null=True)
    email = models.EmailField(max_length=200,null=True,unique=True)
    rollnumber = models.IntegerField(unique=True,null=True)



class course_enrolment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


