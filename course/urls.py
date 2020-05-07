from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:course_id>/totalstudents',views.totalstudents,name='totalstudents'),
    path('<int:course_id>/<int:student_id>/enroll', views.enroll, name='enroll'),
    path('addcourse/<slug:name>', views.addcourse,name = 'addcourse'),
    path('addstudent/<slug:name>', views.addstudent,name = 'addstudent'),
    path('updatecoursename/<int:course_id>/<slug:name>',views.updatecoursename,name = 'updatecoursename'),
    path('updatestudentname/<int:student_id>/<slug:name>',views.updatestudentname,name = 'updatestudentname'),

]