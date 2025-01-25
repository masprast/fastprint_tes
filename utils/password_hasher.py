#!/usr/bin/env python3

# Script utk membuat md5 hash dari password yg ditentukan pada soal

import datetime
import hashlib
import os
from django.http import response
from pathlib import Path

from environ import environ

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, "backend_tes", ".env"))

# api_tes = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'
api_tes = env("SERVERAPI")
# respon_api =response.HttpResponse.request.get('x-form-data')

sekarang = datetime.date.today().strftime("%m-%d-%y")
paswod = "bisacoding-" + sekarang

hasil = hashlib.md5(paswod.encode())

hexhasil = hasil.hexdigest()

print("username untuk hari ini:")
print("(md5) password untuk hari ini:", str(hexhasil))
