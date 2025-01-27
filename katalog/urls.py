from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"produk", views.ListProduk, basename="produk")
router.register("kategori", views.ListKategori)
router.register("status", views.ListStatus)
# router.register("initdb", views.InitDB)

urlpatterns = [
    path("katalog/", include(router.urls)),
]
