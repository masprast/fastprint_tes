from django.db import models

# Create your models here.
class Kategori(models.Model):
    id_kategori = models.IntegerField(primary_key = True, auto_created = True)
    nama_kategori = models.CharField(max_length = 80,unique=True)

    def __str__(self) -> str:
        return f"{self.nama_kategori}"


class Status(models.Model):
    id_status = models.IntegerField(primary_key = True, auto_created = True)
    nama_status = models.CharField(max_length = 80,unique=True)

    def __str__(self) -> str:
        return f"{self.nama_status}"


class Produk(models.Model):
    id_produk = models.IntegerField(primary_key = True,auto_created=True)
    nama_produk = models.CharField(max_length = 255)
    harga = models.IntegerField()
    kategori_id = models.ForeignKey(Kategori,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.id_produk},{self.nama_produk},{self.harga},{self.kategori_id},{self.status_id}"
