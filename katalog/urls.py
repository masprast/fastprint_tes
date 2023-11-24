from django.urls import path
from . import views

urlpatterns = [
    # path('produk/',views.daftar_produk) # type: ignore
    path('produk/',views.ListProduk.as_view())
]
