from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'app/store.html', context)


def cart(request):
    context = {}
    return render(request, 'app/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'app/checkout.html', context)