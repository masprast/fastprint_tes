from django.core.validators import RegexValidator, MinLengthValidator
from .models import Kategori, Produk, Status
from rest_framework import serializers


class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = ["id_kategori", "nama_kategori"]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id_status", "nama_status"]


class ProdukSerializer(serializers.ModelSerializer):
    nama_produk = serializers.CharField(
        validators=[
            MinLengthValidator(limit_value=1, message="nama produk tidak boleh kosong")
        ]
    )
    harga = serializers.CharField(
        validators=[
            RegexValidator(regex=r"^\d+$", message="hanya boleh diisi dengan angka")
        ]
    )

    class Meta:
        model = Produk
        fields = [
            "id_produk",
            "nama_produk",
            "harga",
            "kategori",
            "status",
        ]
        extra_kwargs = {
            "harga": {},
            "kategori": {"write_only": True},
            "status": {"write_only": True},
        }

    def validasi_harga(self, value):
        if value <= 0:
            raise serializers.ValidationError("harga tidak boleh 0.")
        return value

    def to_representation(self, instance):
        representasi = super().to_representation(instance)
        representasi["harga"] = instance.harga
        representasi["no"] = instance.id_produk + 1
        representasi["kategori"] = instance.kategori.nama_kategori
        representasi["status"] = instance.status.nama_status
        return representasi
