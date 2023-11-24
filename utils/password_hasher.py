#!/usr/bin/env python3

# Script utk membuat md5 hash dari password yg ditentukan pada soal

import datetime
import hashlib

sekarang = datetime.date.today().strftime("%m-%d-%y")
paswod = "bisacoding-" + sekarang

hasil = hashlib.md5(paswod.encode())

hexhasil = hasil.hexdigest()

print("(password) hex md5: " + str(hexhasil))