import time


accounts = {
    'username': '1',
    'password': '2',
    'accountNumber': '1',
    'accountMoney': 100,
    'accountNumber2': '2'
}


# Giris Kismi


username = input('Username giriniz :')
password = input('Password giriniz :')


if username==accounts['username'] and password==accounts['password']:
    print('Giris yapiliyor lutfen bekleyiniz..')
    giris = True
else:
    print('Kullanici adi ya da sifre yanlis.')

if giris==True:
    time.sleep(1.5)
    islem = input('Yapmak istediginiz islem nedir? Para gondermek icin 1, Bakiyenizi goruntulemek icin 2 : ')
if islem=='1':
    hesapNumarasiGir = input('Gondermek istediginiz kisinin hesap numarasini giriniz : ')
if islem=='2':
    print(accounts['accountMoney'])
if hesapNumarasiGir==accounts['accountNumber2']:
    miktar = int(input('Miktar giriniz : '))
if miktar < accounts['accountMoney']:
    print('Para gonderildi.')
else:
    print('Yetersiz bakiye')

