from django.shortcuts import render
from first_app.models import Topic, Webpage, Content, Category, Course


# Create your views here.

def webpage(request):
    webpage_list = Webpage.objects.order_by('name')
    web_dict = {'webpages': webpage_list}
    return render(request, 'first_app/webpage.html', context=web_dict)


def topic(request):
    topic_list = Topic.objects.order_by('top_name')
    top_dict = {'topics': topic_list}
    return render(request, 'first_app/topic.html', context=top_dict)


def content(request):
    content_list = Content.objects.order_by('webpage')
    cont_dict = {'contents': content_list}
    return render(request, 'first_app/topic.html', context=cont_dict)


def homepages(request):
    course_list_program = Course.objects.order_by('name')
    part = int(len(course_list_program)/2)
    lst1 = []
    for i in range(0, part, 1):
        lst1.append(course_list_program[i])
    lst2 = []
    for i in range(part, len(course_list_program), 1):
        lst2.append(course_list_program[i])

    course_list_ds = Course.objects.order_by('name')
    part2 = int(len(course_list_ds)/2)
    lst3 = []
    for i in range(0, part2, 1):
        lst3.append(course_list_ds[i])
    lst4 = []
    for i in range(part2, len(course_list_ds), 1):
        lst4.append(course_list_ds[i])

    course_dict = {"courses": course_list_program, "courses_ds": course_list_ds,
                   "course1": lst1, "course2": lst2, "course3": lst3, "course4": lst4}

    return render(request, "first_app/homepages.html", context=course_dict)


def course_detail(request, id=None):
    course = Course.objects.get(pk=id)

    return render(request, "first_app/course_detail.html", context={"course": course})
