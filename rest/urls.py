from django.contrib import admin
from django.urls import path, include 
from checkapi import views
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token
from checkapi.auth import CustomAuthToken


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

# register student view set with router
router.register('student', views.StudentViewSet, basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
     
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
    
    # path('gettoken/', CustomAuthToken.as_view()),
     
    # path('student/', views.student_list),
    # path('student/', views.StudentAPI.as_view()),
    # path('student/<int:id>/', views.StudentAPI.as_view()),
    path('stl/', views.LCStudentList.as_view()),
    path('stl/<int:pk>/', views.URDStudent.as_view()),
    # path('st/', views.student),
    path('st/<int:pk>/', views.student),
    # path('student/', views.student_api),
    path('student_create/', views.student_create),
    path('student/<int:id>/', views.student_detail),
    # path('', include('downloader.urls')),
]
