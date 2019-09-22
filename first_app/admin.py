from django.contrib import admin
from first_app.models import Topic, Webpage, Content, Category, Course
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Content)
admin.site.register(Category)
admin.site.register(Course)
