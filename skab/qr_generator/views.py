from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .productForm import Product_form
from .models import Product, Categorie, Customer, Sale_item, Stock, Sales
import qrcode
# Create your views here.



def index(request):
    if request.user.is_authenticated:
        products = Product.objects.all()

        return render(request, "qr_generator/qr_index.html", {
            "products": products
        })
    else:
        return HttpResponseRedirect(reverse('login'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("qr_index"))
        else:
            return render(request, "qr_generator/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "qr_generator/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def new_product_view(request):

    if request.method == "POST":
        form = Product_form(request.POST)

        if form.is_valid():
            product_name = form.cleaned_data["product_form"]
            description = form.cleaned_data["description"]
            sku = form.cleaned_data["sku"]
            price = form.cleaned_data["price"]
            size = form.cleaned_data["size"]
            color = form.cleaned_data["color"]
            shade = form.cleaned_data["shade"]
            material = form.cleaned_data["material"]
            imageURL = form.cleaned_data["imageURL"]


            product_check = Product.objects.filter(sku=sku)
            if product_check.count() != 1:
                product_obj = Product(
                    product_name=product_name,
                    description=description,
                    sku=sku,
                    price=price,
                    size=size,
                    color=color,
                    shade=shade,
                    material=material,
                    imageURL=imageURL
                )
                product_obj.save()
            else:
                # if already SKU already present then return populated form with enterend data in order to modify
                return HttpResponseRedirect(reverse("new_product", kwargs={
                    "form": form
                }))
    else:
        # return new form
        form = Product_form()
        return render(request, "qr_generator/new_product.html", {
            "form": form
        })
    
def generate_qr_view(request, sku_code):
    data = sku_code
    qr_code = qrcode.make(data)
    path = "website/static/website/qr_codes/"
    file_name = f"{sku_code}.png"
    full_file_path = path+file_name
    qr_code.save(full_file_path)

    return HttpResponseRedirect(reverse('qr_index'))