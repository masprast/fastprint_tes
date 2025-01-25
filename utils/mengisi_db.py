#!/usr/bin/env python3

# ############################################################# #
#                                                               #
#   Script ini berfungsi untuk mengisi data katalog produk ke   #
#   dalam DB Postgre yg dikonfigurasi dalam Docker/cloud        #
#   !!! jalankan script ini hanya SATU kali saja! !!!           #
#                                                               #
# ############################################################# #

import json
import psycopg2
import os
from pathlib import Path
from environ import environ

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, "backend_tes", ".env"))
# cek lokasi file .env
print("lokasi .env: " + os.path.join(BASE_DIR, "backend_tes", ".env"))

# from katalog import models, serializer


class ProdukJSONClass(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class ObjekProduk(object):
    def __init__(
        self, no, id_produk, nama_produk, kategori, harga, status, *args, **kwargs
    ) -> None:
        self.no = no
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.status = status

    def __str__(self) -> str:
        return f"no: {self.no}, id_produk: {self.id_produk}, nama_produk: {self.nama_produk}, kategori: {self.kategori}, harga: {self.harga}, status: {self.status}"


f = open("restapi.json")
obj_f = json.dumps(f, cls=ProdukJSONClass)
data = json.load(f)["data"]
daftar_objek = []
for i in data:
    daftar_objek.append(ObjekProduk(**i))

# cek hasil konverter
print(daftar_objek[1].__str__())

# menghubungi server postgre
server = psycopg2.connect(
    database=env("DB_NAME"),
    user=env("DB_USER"),
    password=env("DB_PASS"),
    host=env("DB_HOST"),
    port=env("DB_PORT"),
)
server.autocommit = False
cursor = server.cursor()

# menyimpan data ke tabel
for produk in daftar_objek:
    # k = models.Kategori.objects.create(nama_kategori = produk.kategori)
    # k.save()
    # s = models.Status.objects.create(nama_status = produk.status)
    # s.save()
    # p = models.Produk.objects.create(
    #     id_produk = produk.id_produk,
    #     nama_produk = produk.nama_produk,
    #     harga = produk.harga,
    #     kategori = models.Kategori.objects.get(nama_kategori=produk.kategori),
    #     status = models.Status.objects.get(nama_status=produk.status)
    #     )
    # p.save()
    print(produk)
    # cursor.execute(f'''
    #     INSERT INTO KATEGORI(NAMA_KATEGORI)
    #     VALUES ({produk.kategori})
    #     ''')
    # cursor.execute(f'''
    #     INSERT INTO STATUS(NAMA_STATUS)
    #     VALUES ({produk.status})
    #     ''')
    # cursor.execute(f'''
    #     INSERT INTO PRODUK(ID_PRODUK, NAMA_PRODUK, HARGA, KATEGORI_ID, STATUS_ID)
    #     VALUES ({produk.id_produk},{produk.nama_produk},{produk.harga},{produk.kategori},{produk.status})
    #     ''')

cursor.executemany("insert into kategori(nama_kategori)", daftar_objek)
cursor.executemany("insert into status(nama_status)", daftar_objek)
cursor.executemany(
    """
    insert into produk(id_produk, nama_produk, harga, kategori_id, status_id)
    values (%i,%s,%s,%s,%s,)
    """,
    daftar_objek,
)

# menyimpan perubahan
server.commit()

# menutup koneksi server
server.close()
