from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
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
    filterset_fields = ["status"]


class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# class InitDB(viewsets.GenericViewSet):
