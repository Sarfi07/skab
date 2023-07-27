from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, "qr_generator/qr_index.html")
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