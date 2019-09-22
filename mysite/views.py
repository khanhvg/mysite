from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContact
from datetime import datetime

# Create your views here.

def index(request):
    # return HttpResponse("Hello everybody")
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    response = render(request, "mysite/index.html", context={'num_visits': num_visits})
    date1 = datetime.now()
    response.set_cookie('visit_time', date1.strftime('%d-%m-%Y %H:%M:%S'))
    return response
def about(request):
    # return HttpResponse("Hello everybody")
    value = request.COOKIES.get('visit_time')
    return render(request, "mysite/about.html", {'noidung':value})


def contact(request):
    registered = False
    if request.method == "POST":
        form_contact = FormContact(data=request.POST)
        if form_contact.is_valid():
            registered = form_contact.save()
            registered.save()
            registered = True
    else:
        form_contact = FormContact()

    response = render(request, "mysite/contact.html", {'contact_form': form_contact, 'registered': registered})
    response.delete_cookie('visit_time')
    return response
