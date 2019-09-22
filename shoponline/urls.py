from django.conf.urls import url
from django.urls import path
from . import views

app_name = "shoponline"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),
    path('course_result/', views.course_result, name='course_result'),
    path('register/', views.register, name='register'),
]
