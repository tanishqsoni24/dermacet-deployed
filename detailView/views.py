from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Career, LevelManufacturing
from accounts.models import Profile, Cart
from shop.models import Product, Category
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    #Fetching Popular Products
    popular_products = list(Product.objects.all().order_by('-buy_count')[:4])
    new_products = list(Product.objects.all().order_by('-created_at')[:4])
    random.shuffle(popular_products)
    categories = Category.objects.all()

    # Fetching Cart Items

    if(request.user.is_authenticated):
        carts = Cart.objects.filter(is_paid = False, user = request.user)
        cart_items = []
        delete = False
        for cart in carts:
            for cart_item in cart.cart_items.all():
                if cart_item.product.product_available_count > 0:
                    cart_items.append(cart_item)
                else:
                    cart_item.delete()
                    delete = True

        return render(request, "detailView/index.html",{'popular_products':popular_products, 'new_products': new_products, 'home_page':True, 'categories':categories, 'cart_items':cart_items, 'cart':carts})
    return render(request, "detailView/index.html",{'popular_products':popular_products, 'new_products': new_products, 'home_page':True, 'categories':categories})
def contctus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("message")
        contact_data = Contact(name=name, email=email, message=msg)
        contact_data.save()
        messages.success(request, "Your Request has been submitted successfully")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "detailView/contactus.html")


def career(request):
    if request.user.is_authenticated:
        if request.method == "POST" and request.FILES['CV']:
            name = request.POST['name']
            email = request.POST['email']
            cv = request.FILES['CV']
            career_data = Career(name=name, email=email, cv=cv)
            career_data.save()
            profile = Profile.objects.filter(user=request.user).first()
            profile.is_cv_uploaded = True
            profile.save()
            messages.success(request, "Your Request has been submitted successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if list(Profile.objects.filter(user=request.user).values('is_cv_uploaded'))[0].get('is_cv_uploaded'):
            return render(request, "detailView/career.html", {'is_cv_uploaded':True})
        messages.warning(request, "Autofilled your details from your profile! Please correct if any wrong")
        return render(request, "detailView/career.html")
    else:
        messages.warning(request, "Please Login First")
        return redirect('accounts/login')   
    
def level_manufacturing(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_num")
        interested_in = request.POST.get("interested")
        types_of_products = request.POST.get("Types")
        planning_to_choose = request.POST.get("timetochoose")
        message = request.POST.get("message")
        level_manufacturing = LevelManufacturing(
            name=full_name,
            email=email,
            contact_num=phone_number,
            interested_in=interested_in,
            types_of_products=types_of_products,
            planning_to_choose=planning_to_choose,
            message=message
        )
        level_manufacturing.save()
        messages.success(request, "Your Request has been submitted successfully")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "detailView/level_manufacturing.html")