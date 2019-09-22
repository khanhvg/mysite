from django.shortcuts import render
from .models import Product
from cart.forms import CartAddProductForm
from .forms import UserForm, UserProfileInfoForm
from . import forms


# Create your views here.

def home(request):
    product_list = Product.objects.order_by('name')
    product_dict = {'products': product_list}

    return render(request, "shoponline/home.html", context=product_dict)


def course_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = CartAddProductForm()
    return render(request, "shoponline/course_detail.html",
                  context={"product": product, 'cart_product_form': cart_product_form})


def course_result(request):
    product_list = Product.objects.order_by('name')
    print(product_list)
    product_result = []
    count = 0
    if request.method == "GET":
        sanpham = request.GET.get("sanpham")
    for product in product_list:
        if sanpham.lower() in product.name.lower():
            product_result.append(product)
    if len(product_result) > 0:
        count = len(product_result)
    return render(request, "shoponline/course_result.html", context={"product_result": product_result, "count": count})


def register(request):
    registered = False
    if request.method == "POST":
        form_user = forms.UserForm(data=request.POST)
        form_por = forms.UserProfileInfoForm(data=request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()

            profile = form_por.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = forms.UserForm()
        form_por = forms.UserProfileInfoForm()

    return render(request, "shoponline/register.html",
                  {'user_form': form_user, 'profile_form': form_por, 'registered': registered})
