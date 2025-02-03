from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import KategoriViewSet, ProdukViewSet, StatusViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r"produk", ProdukViewSet, basename="produk")
router.register(r"kategori", KategoriViewSet, basename="kategori")
router.register(r"status", StatusViewSet, basename="status")
# router.register("initdb", views.InitDB)

urlpatterns = [
    path("", include(router.urls)),
]
