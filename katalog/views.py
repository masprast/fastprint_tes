from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Kategori, Produk, Status
from .serializer import (
    KategoriSerializer,
    StatusSerializer,
    ProdukSerializer,
)


# Create your views here.
class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all().order_by("id_produk")
    serializer_class = ProdukSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["kategori", "status"]

    # def filter_queryset(self, queryset):
    #     queryset = Produk.objects.filter(status=2).order_by("id_produk")
    #     return super().filter_queryset(queryset)


# class AllProdukViewSet(viewsets.ModelViewSet):
#     queryset = Produk.objects.all().order_by("id_produk")
#     serializer_class = ProdukSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ["status", "kategori"]


class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
