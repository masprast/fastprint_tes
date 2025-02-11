# Tes Programming Backend

Repositori ini ditujukan untuk proses rekrutmen untuk posisi _backend developer_. _Tech stack_ yang digunakan untuk repo ini adalah **Django** dan **Docker**.

Demo ada di alamat [railway.app](https://fastprinttes-production.up.railway.app/api)

## Prerequisites

Berikut paket-paket yang dibutuhkan dalam pembuatan API:

1. Python `--` 3.10
2. virtualenv `--` 20.13
3. [Docker](https://docs.docker.com/desktop) `--` 24.0
4. [Docker Compose](https://docs.docker.com/compose/install/) `--` 1.29
5. pip `--` 22.0

- sedangkan editor yang digunakan adalah **VSCode**.

> Sebelum melakukan pengetesan pastikan paket-paket yang dibutuhkan telah terinstall.

---

Selanjutnya silahkan kloning repo ini ke dalam sebuah folder.

1. buat folder untuk menampung repo. ( **_updated_** )

   ```sh
   mkdir fastprint_tes
   cd fastprint_tes
   ```

   > penulis menggunakan sistem operasi Linux, untuk sistem operasi lain, silahkan menyesuaikan

2. kloning repo dari github.com. ( **_updated_** )

   ```sh
   git clone https://github.com/masprast/fastprint_tes .
   ```

---

### Testing

Selanjutnya adalah menjalankan aplikasi yang telah saya isolasi dengan Docker.

```sh
docker-compose up --build &
```

> Perintah di atas akan menjalankan sekaligus mengkonfigurasi Django dan Postgre

Selanjutnya jalankan web browser lalu buka alamat `localhost:8000/api` ATAU dapat mencoba live demo yang telah saya deploy di [railway.app](https://fastprinttes-production.up.railway.app/api/).

---

### Testing API CRUD

Langkah terakhir adalah melakukan testing API CRUD. Berikut adalah daftar url API. Dengan API root: `localhost:8000/api`

> \*NOTE: Edit terlebih dahulu file **/backend_tes/.env** dengan memberi _value_ pada tiap VAR.

### Produk

#### Daftar semua produk

- Endpoint: `produk/`
- Method: **GET**
- Query: -
- Data: -
- Response:

```json
[
	{
		"id_produk": 6,
		"nama_produk": "ALCOHOL GEL POLISH CLEANSER GP-CLN01",
		"harga": 12500,
		"no": 7,
		"kategori": "L QUEENLY",
		"status": "bisa dijual"
	},
	{
		"id_produk": 9,
		"nama_produk": "ALUMUNIUM FOIL ALL IN ONE BULAT 23mm IM",
		"harga": 1000,
		"no": 10,
		"kategori": "L MTH AKSESORIS (IM)",
		"status": "bisa dijual"
	}
	//   ...
]
```

#### Daftar produk dengan filter status

- Endpoint: `produk/`
- Method: **GET**
- Query: `?status=2`
- Data: -
- Response:

```json
[
	{
		"id_produk": 12,
		"nama_produk": "ALUMUNIUM FOIL ALL IN ONE SHEET 250mm IM",
		"harga": 12500,
		"no": 13,
		"kategori": "L MTH AKSESORIS (IM)",
		"status": "tidak bisa dijual"
	},
	{
		"id_produk": 18,
		"nama_produk": "ALUMUNIUM FOIL HDPE/PE SHEET 250mm IM",
		"harga": 13000,
		"no": 19,
		"kategori": "L MTH AKSESORIS (IM)",
		"status": "tidak bisa dijual"
	}
	//   ...
]
```

#### Buat produk

- Endpoint: `produk/`
- Method: **POST**
- Query: -
- Data:

```json
{
	"nama_produk": "cat",
	"harga": 33000,
	"kategori": "6",
	"status": "1"
}
```

- Response:

```json
{
	"id_produk": 1,
	"nama_produk": "cat",
	"harga": "33000",
	"no": 2,
	"kategori": "L MTH TABUNG (LK)",
	"status": "tidak bisa dijual"
}
```

#### Ubah produk

- Endpoint: `produk/<int:id_produk>`
- Method: **PUT**
- Query: -
- Data:

```json
{
	"nama_produk": "cat tembok",
	"harga": 33000,
	"kategori": "3",
	"status": "1"
}
```

- Response:

```json
{
	"id_produk": 1,
	"nama_produk": "cat tembok",
	"harga": "33000",
	"no": 2,
	"kategori": "L MTH TABUNG (LK)",
	"status": "bisa dijual"
}
```

#### Hapus produk

- Endpoint: `produk/<int:id_produk>`
- Method: **DELETE**
- Query: -
- Data: -
- Response: -

### Kategori

#### Daftar semua kategori

- Endpoint: `kategori/`
- Method: **GET**
- Query: -
- Data: -
- Response:

```json
[
	{
		"id_kategori": 1,
		"nama_kategori": "S MTH STEMPEL (IM)"
	},
	{
		"id_kategori": 2,
		"nama_kategori": "CI MTH TINTA LAIN (IM)"
	}
	//   ...
]
```

#### Buat kategori

- Endpoint: `kategori/`
- Method: **POST**
- Query: -
- Data:

```json
{
	"nama_kategori": "kategori A"
}
```

- Response:

```json
{
	"id_kategori": 8,
	"nama_kategori": "kategori A"
}
```

#### Ubah kategori

- Endpoint: `kategori/<int:id_kategori>`
- Method: **PUT**
- Query: -
- Data:

```json
{
	"nama_kategori": "kategori AA"
}
```

- Response:

```json
{
	"id_kategori": 8,
	"nama_kategori": "kategori AA"
}
```

#### Hapus kategori

- Endpoint: `kategori/<int:id_kategori>`
- Method: **DELETE**
- Query: -
- Data: -
- Response: -

### Status

#### Daftar semua status

- Endpoint: `status/`
- Method: **GET**
- Query: -
- Data: -
- Response:

```json
[
	{
		"id_status": 1,
		"nama_status": "tidak bisa dijual"
	},
	{
		"id_status": 2,
		"nama_status": "bisa dijual"
	}
]
```

#### Buat status

- Endpoint: `status/`
- Method: **POST**
- Query: -
- Data:

```json
{
	"nama_status": "ada stok"
}
```

- Response:

```json
{
	"id_status": 3,
	"nama_status": "ada stok"
}
```

#### Ubah status

- Endpoint: `status/<int:id_status>`
- Method: **PUT**
- Query: -
- Data:

```json
{
	"nama_status": "ada barang"
}
```

- Response:

```json
{
	"id_status": 3,
	"nama_status": "ada barang"
}
```

#### Hapus status

- Endpoint: `status/<int:id_status>`
- Method: **DELETE**
- Query: -
- Data: -
- Response: -
