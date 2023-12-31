from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='qr_index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'), 
    path('new_product', views.new_product_view, name="new_product"),
    path("generate_qr/<str:sku_code>", views.generate_qr_view, name="generate_qrcode")
]