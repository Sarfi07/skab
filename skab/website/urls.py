from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('new_bill', views.new_bill_view, name="new_bill"),
    path('stock', views.stock_view, name="stock"),
    path('history', views.history_view, name='history'),
    path('about', views.about_view, name="about"),
    path('skuObj/<str:sku>', views.skuObj_view, name="skuObj"),
]