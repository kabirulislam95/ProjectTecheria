from django.db.models.fields import NullBooleanField
from django.http import response
from django.shortcuts import redirect, render
from techeria_app.models import BuyerModel, SellerModel, Products, Laptops,Smartphone
from django.contrib.auth.models import User, auth

from django.contrib import messages


# Create your views here.
def index(request):
    product = Products.objects.all()
    context = {
        'product': product
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def laptop(request):
    laptop = Laptops.objects.all()
    context = {
        'laptop': laptop
    }
    return render(request, 'laptop.html', context)

def smartphone(request):
    smartphone = Smartphone.objects.all()
    context = {
        'smartphone': smartphone
    }
    return render(request, 'smartphone.html', context)
    
def loginpage(request):
    return render(request, 'loginpage.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def registration(request):
    return render(request, 'registration.html')

def search(request):
    q = request.GET['q']
    data = Products.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'data': data})
def product(request):
    return render(request, 'product.html')

def productInfo(request, i):
    oneProduct = Products.objects.get(id=i)
    context = {
        'oneProduct': oneProduct
    }
    return render(request, 'productInfo.html', context)

def registration(request):


    if request.method == 'POST':
        first_name = request.POST ['First_Name']
        last_name = request.POST ['Last_Name']
        date_of_birth = request.POST ['Date_of_Birth']
        email = request.POST ['Email_Id']
        mobile_number = request.POST ['Mobile_Number']
        address = request.POST['Address']
        user_name = request.POST['Username']
        city = request.POST ['City']
        state = request.POST ['State']
        zip_code = request.POST ['Zip_Code']
        country = request.POST ['Country']
        password = request.POST ['Password']
        confirm_password = request.POST ['Confirm_Password']
        category = request.POST.get ('kk')

        buyer = BuyerModel()
        seller = SellerModel()







# Create your views here.
def index(request):
    product = Products.objects.all()
    context = {
        'product': product
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def watch(request):
    return render(request, 'watch.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def registration(request):
    return render(request, 'registration.html')

def search(request):
    q = request.GET['q']
    data = Products.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'data': data})
def product(request):
    return render(request, 'product.html')

def registration(request):
    if request.method == 'POST':
        first_name = request.POST ['First_Name']
        last_name = request.POST ['Last_Name']
        date_of_birth = request.POST ['Date_of_Birth']
        email = request.POST ['Email_Id']
        mobile_number = request.POST ['Mobile_Number']
        address = request.POST['Address']
        username = request.POST['Username']
        city = request.POST ['City']
        state = request.POST ['State']
        zip_code = request.POST ['Zip_Code']
        country = request.POST ['Country']
        password = request.POST ['Password']
        confirm_password = request.POST ['Confirm_Password']
        category = request.POST.get ('kk')

        buyer = BuyerModel()
        seller = SellerModel()

        if password == confirm_password:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username has already been taken")
                return redirect("registration")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "You already have an account please login")
                return redirect("registration")

            else:


                if category == "Buyer":
                    buyer.username = username
                    buyer.first_name=first_name
                    buyer.last_name=last_name
                    buyer.username=username
                    buyer.email=email;
                    buyer.date_of_birth=date_of_birth
                    buyer.mobile_number=mobile_number
                    buyer.address=address
                    buyer.city=city
                    buyer.state=state
                    buyer.zip_code=zip_code
                    buyer.country=country
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    buyer.save()
                    user.save()
                    return redirect("/")

                elif category == "Seller":
                    seller.user_name = username
                    seller.first_name=first_name
                    seller.last_name=last_name
                    seller.username=username
                    seller.email=email;
                    seller.date_of_birth=date_of_birth
                    seller.mobile_number=mobile_number
                    seller.address=address
                    seller.city=city
                    seller.state=state
                    seller.zip_code=zip_code
                    seller.country=country
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    seller.save()
                    user.save()
                    return redirect("/")
                else:
                    return render(request, '.html')
        else:
            messages.info(request, "Password does not match")
            return redirect("registration")

    else:

        return render(request, 'registration.html')
