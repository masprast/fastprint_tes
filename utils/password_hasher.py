#!/usr/bin/env python3

# Script utk membuat md5 hash dari password yg ditentukan pada soal

import datetime
import hashlib
from django.http import response

api_tes = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
# respon_api =response.HttpResponse.request.get('x-form-data')

sekarang = datetime.date.today().strftime("%m-%d-%y")
paswod = "bisacoding-" + sekarang

hasil = hashlib.md5(paswod.encode())

hexhasil = hasil.hexdigest()

print("username untuk hari ini:")
print("(md5) password untuk hari ini:", str(hexhasil))