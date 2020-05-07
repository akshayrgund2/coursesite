from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/coursedetails',views.coursedetails,name='coursedetails'),
    path('<int:student_id>/studentdetails',views.studentdetails,name='studentdetails'),
    path('<int:course_id>/<int:student_id>/enroll', views.enroll, name='enroll'),
    path('addcourse/<slug:name>', views.addcourse,name = 'addcourse'),
    path('addstudent/<slug:name>', views.addstudent,name = 'addstudent'),
    path('updatecoursename/<int:course_id>/<slug:name>',views.updatecoursename,name = 'updatecoursename'),
    path('updatestudentname/<int:student_id>/<slug:name>',views.updatestudentname,name = 'updatestudentname'),
    path('<int:student_id>/deletestudent',views.deletestudent,name = 'deletestudent'),
    path('<int:course_id>/deletecourse',views.deletecourse,name = 'deletecourse'),

]