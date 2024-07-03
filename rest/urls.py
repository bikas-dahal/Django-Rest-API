from django.contrib import admin
from django.urls import path, include 
from checkapi import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', views.student_list),
    path('student/', views.StudentAPI.as_view()),
    path('student/<int:id>/', views.StudentAPI.as_view()),
    path('stl/', views.LCStudentList.as_view()),
    path('stl/<int:pk>/', views.URDStudent.as_view()),
    # path('st/', views.student),
    path('st/<int:pk>/', views.student),
    # path('student/', views.student_api),
    path('student_create/', views.student_create),
    path('student/<int:id>/', views.student_detail),
    # path('', include('downloader.urls')),
]
