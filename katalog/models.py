from django.db import models

# Create your models here.
class Kategori(models.Model):
    id_kategori = models.AutoField( primary_key = True)
    nama_kategori = models.CharField(max_length = 80,unique=True)

    class Meta:
        db_table = 'kategori'

    def __str__(self) -> str:
        return f"{self.id_kategori}"


class Status(models.Model):
    id_status = models.AutoField( primary_key = True)
    nama_status = models.CharField(max_length = 80,unique=True)

    class Meta:
        db_table = 'status'

    def __str__(self) -> str:
        return f"{self.id_status}"


class Produk(models.Model):
    id_produk = models.IntegerField(auto_created = True, unique=True, primary_key = True)
    nama_produk = models.CharField(max_length = 255)
    harga = models.IntegerField()
    kategori_id = models.ForeignKey(Kategori,on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        db_table = 'produk'

    def __str__(self) -> str:
        return f"{self.id_produk}"

    def toString(self):
        return f"{self.id_produk},{self.nama_produk},{self.harga},{self.kategori_id},{self.status_id}"
