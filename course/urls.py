from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/coursedetails',views.coursedetails,name='coursedetails'),
    path('<int:student_id>/studentdetails',views.studentdetails,name='studentdetails'),
    path('enroll', views.enroll, name='enroll'),
    path('enrollform', views.enrollform, name='enrollform'),
    path('addcourse', views.addcourse,name = 'addcourse'),
    path('addcourseform', views.addcourseform,name = 'addcourseform'),
    path('addstudent', views.addstudent,name = 'addstudent'),
    path('addstudentform', views.addstudentform,name = 'addstudentform'),
    path('updatecoursename/<int:course_id>/<slug:name>',views.updatecoursename,name = 'updatecoursename'),
    path('updatestudentname/<int:student_id>/<slug:name>',views.updatestudentname,name = 'updatestudentname'),
    path('<int:student_id>/deletestudent',views.deletestudent,name = 'deletestudent'),
    path('<int:course_id>/deletecourse',views.deletecourse,name = 'deletecourse'),

]