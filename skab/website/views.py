from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "website/index.html")


def new_bill_view(request):

    if request.method == "GET":
        return render(request, "website/new_bill.html")
    else:
        pass