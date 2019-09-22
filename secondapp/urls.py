from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'secondapp'
urlpatterns = [
    path('webpage/', views.webpage, name='webpage'),
    path('topic/', views.topic, name='topic'),
]
