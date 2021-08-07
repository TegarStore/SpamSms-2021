import json
import requests
import os
import sys

def main():
        os.system('clear')
        os.system('figlet Spam Sms')
        banner = '''
[+]======================================[+]
   + Author : Tegar Store
   + Youtube : Tegar Gaming
   + Github : https://github.com/TegarStore
[+]======================================[+]
'''

       print(banner)
       no = input('target : ')
       jum = input('Jumlah Spam : ')

       head = {
       "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A>
       "Referer": "https://www.mapclub.com/en/user/signup",
       Host": "cmsapi.mapclub.com",
       }


       dat = {
       'phone': no
       }

       dat = {
       'phone': no
       }

       for x in range(int(jum)):
               leosureo = requests.post("https://cmsapi.ma>
               if 'eror' in leosureo:
                      print(' Gagal  Mengirim '+ no)
               else
                      print(' Sukses Mengirim '+ no)

main()