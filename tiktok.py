#!/usr/bin/env python3

import sys
import os
import requests as rq
from bs4 import BeautifulSoup as bs

os.system("clear")

b = """

 /$$$$$$$$ /$$ /$$         /$$               /$$      
|__  $$__/|__/| $$        | $$              | $$      
   | $$    /$$| $$   /$$ /$$$$$$    /$$$$$$ | $$   /$$
   | $$   | $$| $$  /$$/|_  $$_/   /$$__  $$| $$  /$$/
   | $$   | $$| $$$$$$/   | $$    | $$  \ $$| $$$$$$/ 
   | $$   | $$| $$_  $$   | $$ /$$| $$  | $$| $$_  $$ 
   | $$   | $$| $$ \  $$  |  $$$$/|  $$$$$$/| $$ \  $$
   |__/   |__/|__/  \__/   \___/   \______/ |__/  \__/

                  Tiktok Profiling

                  Created by Alfin
"""
print(b)

tiktok_user = input("Masukan Username Tiktok : ")
print()
u = "https://tiktok.com/@" + tiktok_user
r = rq.get(u)
if r.status_code == 200:
    print("Akun ditemukan : ")
    print()
    print(f"> Link Akun : {u}")
    print()
elif r.status_code == 404:
    print("Akun tidak ditemukan")
    sys.exit("\n")
sp = bs(r.content, 'html.parser')
photo = sp.find("meta",{"property":"og:image"})["content"]
print(f"""> Link Photo : 

{photo}""")
print()

nama = sp.find("h1",{"class":"tiktok-qpyus6-H1ShareSubTitle e198b7gd6"})
print(f"> Nama : {nama.string}")
print()

following = sp.find("h2",{"class":"tiktok-7k173h-H2CountInfos e1awr0pt0"})
flw = following.find("div",{"class":"tiktok-xeexlu-DivNumber e1awr0pt1"})
flw2 = flw.find("strong",{"data-e2e":"following-count"})
print(f"> Following : {flw2.string}")
print()

followers = sp.find("h2",{"class":"tiktok-7k173h-H2CountInfos e1awr0pt0"})
flwr = followers.find("strong",{"data-e2e":"followers-count"})
print(f"> Followers : {flwr.string}")
print()

likes = sp.find("h2",{"class":"count-infos"})
lk = followers.find("strong",{"title":"Likes"})
print(f"> Likes : {lk.string}")
print()

bio = sp.find("h2",{"class":"tiktok-b1wpe9-H2ShareDesc e1awr0pt3"})
print(f"> Bio : {bio.string}")
print()

try:
    upload = sp.find("img",{"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})["alt"]
    gv = sp.find("img",{"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})["src"]
    view = sp.find("strong",{"class":"video-count tiktok-1p23b18-StrongVideoCount eor0hs42"})
    print(f"> Upload Terakhir : {upload}")
    print()
    print(f"""> Link Gambar video : ↲
    
{gv}""")
    print()
    print(f"> Viewers : {view.string} ↲")
    print()
except Exception as e:
    sys.exit(">> Akun diprivasi <<\n")
