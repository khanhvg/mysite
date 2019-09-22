from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('webpage/', views.webpage, name='webpage'),
    path('topic/', views.topic, name='topic'),
    path('homepages/', views.homepages, name='homepages'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),
]
