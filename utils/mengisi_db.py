# #!/usr/bin/env python3

# # ############################################################# #
# #                                                               #
# #   Script ini berfungsi untuk mengisi data katalog produk ke   #
# #   dalam DB Postgre yg dikonfigurasi dalam Docker/cloud        #
# #   !!! jalankan script ini hanya SATU kali saja! !!!           #
# #                                                               #
# # ############################################################# #

# import json
# import psycopg2
# import os
# from django.db import IntegrityError
# from pathlib import Path
# from environ import environ
# from katalog import models

# env = environ.Env()

# BASE_DIR = Path(__file__).resolve().parent.parent
# environ.Env.read_env(os.path.join(BASE_DIR, "backend_tes", ".env"))
# # cek lokasi file .env
# print("lokasi .env: " + os.path.join(BASE_DIR, "backend_tes", ".env"))

# # from katalog import models, serializer


# class ProdukJSONClass(json.JSONEncoder):
#     def default(self, o):
#         return o.__dict__


# class ObjekProduk(object):
#     def __init__(
#         self, no, id_produk, nama_produk, kategori, harga, status, *args, **kwargs
#     ) -> None:
#         self.no = no
#         self.id_produk = id_produk
#         self.nama_produk = nama_produk
#         self.kategori = kategori
#         self.harga = harga
#         self.status = status

#     def __str__(self) -> str:
#         return f"no: {self.no}, id_produk: {self.id_produk}, nama_produk: {self.nama_produk}, kategori: {self.kategori}, harga: {self.harga}, status: {self.status}"


# def isiDB():
#     # mengisi DB
#     f = open("restapi.json")
#     # obj_f = json.dumps(f, cls=ProdukJSONClass)
#     data = json.load(f)["data"]
#     daftar_objek = []
#     daftar_kategori = []
#     daftar_status = []
#     for i in data:
#         daftar_objek.append(ObjekProduk(**i))

#     # cek hasil konverter
#     print(len(daftar_objek))

#     # menghubungi server postgre
#     server = psycopg2.connect(
#         database=env("PGDATABASE"),
#         user=env("PGUSER"),
#         password=env("PGPASSWORD"),
#         host=env("PGHOST"),
#         port=env("PGPORT"),
#     )

#     server.autocommit = False
#     # cursor = server.cursor()

#     # menyimpan data ke tabel
#     for k in daftar_objek:
#         if k.kategori not in daftar_kategori:
#             daftar_kategori.insert(0, k.kategori)

#     for s in daftar_objek:
#         if s.status not in daftar_status:
#             daftar_status.insert(0, s.status)

#         for dk in daftar_kategori:
#             try:
#                 k = models.Kategori.objects.create(nama_kategori=dk)
#                 k.save()
#             except IntegrityError:
#                 pass
#             # cursor.execute(
#             #     "insert into katalog_kategori(nama_kategori) values(%s)", k.__str__()
#             # )

#         # cursor.executemany(
#         #     "insert into katalog_kategori(nama_kategori) values(%s)", (daftar_kategori)
#         # )
#         for ds in daftar_status:
#             try:
#                 s = models.Status.objects.create(nama_status=ds)
#                 s.save()
#             except IntegrityError:
#                 pass
#             # cursor.execute(
#             #     "insert into katalog_status(nama_status) values(%s)", (s.__str__())
#             # )
#         # cursor.executemany(
#         #     "insert into katalog_status(nama_status) values(%s)", (daftar_status)
#         # )

#         for produk in daftar_objek:
#             try:
#                 p = models.Produk.objects.create(
#                     id_produk=produk.id_produk,
#                     nama_produk=produk.nama_produk,
#                     harga=produk.harga,
#                     kategori=models.Kategori.objects.get(nama_kategori=produk.kategori),
#                     status=models.Status.objects.get(nama_status=produk.status),
#                 )
#                 p.save()
#             except IntegrityError:
#                 pass

#             # cursor.execute(
#             #     """
#             #     insert into katalog_produk(id_produk, nama_produk, harga, kategori_id, status_id)
#             #     values (%i,%s,%s,%s,%s,)
#             #     """,
#             #     (
#             #         p.id_produk.__str__(),
#             #         p.nama_produk,
#             #         p.harga.__str__(),
#             #         p.kategori_id.__str__(),
#             #         p.status_id.__str__(),
#             #     ),
#             # )

#     # menyimpan perubahan
#     server.commit()

#     # menutup koneksi server
#     server.close()
