import json

class ProdukJSONClass(json.JSONEncoder):
    def default(self,o):
        return o.__dict__

class ObjekProduk(object):
    def __init__(self, no, id_produk, nama_produk, kategori, harga, status, *args, **kwargs) -> None:
        self.no = no
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga
        self.status = status

    def __str__(self) -> str:
        return f"no: {self.no}, id_produk: {self.id_produk}, nama_produk: {self.nama_produk}, kategori: {self.kategori}, harga: {self.harga}, status: {self.status}"


f = open('restapi.json')
daftar_objek = []

def konvert():
    data = json.load(f)['data']
    for i in data:
        daftar_objek.append(ObjekProduk(**i))

def isiKategori(arr_kategori):
    arr_ = []
    for kategori in arr_kategori:
        arr_.append(kategori.kategori)
    return list(set(arr_))

def isiStatus(arr_status):
    arr_ = []
    for status in arr_status:
        arr_.append(status.status)
    return list(set(arr_))