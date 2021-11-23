from techeria_app.models import Products, Laptops, Smartphone
from django.shortcuts import render


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


def search(request):
    q = request.GET['q']
    data = Products.objects.filter(name__icontains=q)
    return render(request, 'search.html', {'data': data})


def productInfo(request, i):
    oneProduct = Products.objects.get(id=i)
    context = {
        'oneProduct': oneProduct
    }
    return render(request, 'productInfo.html', context)


def product(request):
    product = Products.objects.all()
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def registration(request):
    return render(request, 'registration.html')
