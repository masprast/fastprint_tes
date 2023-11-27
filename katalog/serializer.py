from django.core.validators import RegexValidator,MinLengthValidator
from .models import Kategori, Produk, Status
from rest_framework import serializers

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ['nama_kategori']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['nama_status']

class ProdukSerializer(serializers.ModelSerializer):
    nama_produk = serializers.CharField(validators=[
        MinLengthValidator(limit_value=1,message='nama produk tidak boleh kosong')
        ])
    harga = serializers.CharField(validators=[
        RegexValidator(regex=r'^\d+$',message='hanya boleh diisi dengan angka')
        ])

    class Meta:
        model = Produk
        fields = [
            'id_produk',
            'nama_produk',
            'harga',
            'kategori_id',
            'status_id',
        ]
        extra_kwargs = {
            'kategori_id':{'write_only':True},
            'status_id':{'write_only':True}
        }

    def to_representation(self, instance):
        representasi = super().to_representation(instance)
        representasi['no'] = instance.id_produk + 1
        representasi['kategori'] = instance.kategori_id.nama_kategori
        representasi['status'] = instance.status_id.nama_status
        return representasi