from django.shortcuts import render
from django.http import JsonResponse
from  qr_generator.models import Product, Brand, Categorie
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request, "website/index.html")


def new_bill_view(request):

    if request.method == "GET":
        return render(request, "website/new_bill.html")
    else:
        pass

def stock_view(request):

    return render(request, "website/stock.html")

def history_view(request):

    return render(request, "website/history.html")

def about_view(request):

    return render(request, "website/about.html")


def skuObj_view(request, sku):

    skuObj = Product.objects.get(sku=sku)
    data = serialize('json', [skuObj])

    return JsonResponse(data, safe=False)