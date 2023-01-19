import phonenumbers
print('PENDETEKSI LOKASI NOMER HP')
number = input('Masukan Nomer HP dengan format \'+62\': ')

from phonenumbers import geocoder
Negara = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(Negara, "id"))

from phonenumbers import carrier
Servis = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(Servis, "id"))