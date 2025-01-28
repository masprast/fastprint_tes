from rest_framework import viewsets
from .models import Kategori, Produk, Status
from .serializer import KategoriSerializer, ProdukSerializer, StatusSerializer
from utils import mengisi_db


# Create your views here.
class ListProduk(viewsets.ModelViewSet):
    queryset = Produk.objects.filter(status_id=2).order_by("id_produk")
    serializer_class = ProdukSerializer


class ListKategori(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer


class ListStatus(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


# class InitDB(viewsets.GenericViewSet):
#     mengisi_db.isiDB()
