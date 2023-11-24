from .models import Kategori, Produk, Status
from rest_framework import serializers

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = {
            'id_produk'
            'nama_produk'
            'harga'
            'kategori_id'
            'status_id'
        }

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = {'id_kategori','nama_kategori'}

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = {'id_status','nama_status'}