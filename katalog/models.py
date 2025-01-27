from django.db import models


# Create your models here.
class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=80, unique=True)

    def __str__(self) -> str:
        return f"{self.nama_kategori}"


class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=80, unique=True)

    def __str__(self) -> str:
        return f"{self.nama_status}"


class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=255)
    harga = models.IntegerField()
    kategori = models.ForeignKey("Kategori", on_delete=models.CASCADE)
    status = models.ForeignKey("Status", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nama_produk}"

    def toString(self):
        return f"{self.id_produk},{self.nama_produk},{self.harga},{self.kategori},{self.status}"
