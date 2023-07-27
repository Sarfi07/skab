from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('new_bill', views.new_ill_view, name="new_bill")
]