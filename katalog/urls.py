from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, DynamicRoute, SimpleRouter
from .views import KategoriViewSet, StatusViewSet, ProdukViewSet  # AllProdukViewSet


router = DefaultRouter()
router.register(r"produk", ProdukViewSet, basename="produk")
# router.register(r"produkall", AllProdukViewSet, basename="all-produk")
router.register(r"kategori", KategoriViewSet, basename="kategori")
router.register(r"status", StatusViewSet, basename="status")


urlpatterns = [path("", include(router.urls))]
