#!/usr/bin/env python3

import sys
import os
import requests as rq
from bs4 import BeautifulSoup as bs

os.system("clear")

b = """
 \033[31m
 /$$$$$$$$ /$$ /$$         /$$               /$$      
|__  $$__/|__/| $$        | $$              | $$      
   | $$    /$$| $$   /$$ /$$$$$$    /$$$$$$ | $$   /$$
   | $$   | $$| $$  /$$/|_  $$_/   /$$__  $$| $$  /$$/
   | $$   | $$| $$$$$$/   | $$    | $$  \ $$| $$$$$$/ 
   | $$   | $$| $$_  $$   | $$ /$$| $$  | $$| $$_  $$ 
   | $$   | $$| $$ \  $$  |  $$$$/|  $$$$$$/| $$ \  $$
   |__/   |__/|__/  \__/   \___/   \______/ |__/  \__/ \033[0m 

                 \033[36m Tiktok Profiling

                  Created by Alfin \033[0m  
"""
print(b)

tiktok_user = input("\033[31mMasukan Username Tiktok \033[37m: \033[0m")
print()
u = "https://tiktok.com/@" + tiktok_user
r = rq.get(u)
if r.status_code == 200:
    print("Akun ditemukan : ")
    print()
    print(f"\033[37m>\033[0m \033[36mLink Akun \033[37m: {url}\033[0m")
    print()
elif r.status_code == 404:
    print("Akun tidak ditemukan")
    sys.exit("\n")
sp = bs(r.content, 'html.parser')
photo = sp.find("meta",{"property":"og:image"})["content"]
print(f"""\033[37m>\033[0m \033[36mLink Photo \033[37m: 

{photo}\033[0m""")
print()

nama = sp.find("h1",{"class":"tiktok-qpyus6-H1ShareSubTitle e198b7gd6"})
print(f"\033[37m>\033[0m \033[36mNama \033[37m: {nama.string}\033[0m")
print()

following = sp.find("h2",{"class":"tiktok-7k173h-H2CountInfos e1awr0pt0"})
flw = following.find("div",{"class":"tiktok-xeexlu-DivNumber e1awr0pt1"})
flw2 = flw.find("strong",{"data-e2e":"following-count"})
print(f"\033[37m>\033[0m \033[36mFollowing \033[37m: {flw2.string}\033[0m")
print()

followers = sp.find("h2",{"class":"tiktok-7k173h-H2CountInfos e1awr0pt0"})
flwr = followers.find("strong",{"data-e2e":"followers-count"})
print(f"\033[37m>\033[0m \033[36mFollowers \033[37m: {flwr.string}\033[0m")
print()

likes = sp.find("h2",{"class":"count-infos"})
lk = followers.find("strong",{"title":"Likes"})
print(f"\033[37m>\033[0m \033[36mLikes \033[37m: {lk.string}\033[0m")
print()

bio = sp.find("h2",{"class":"tiktok-b1wpe9-H2ShareDesc e1awr0pt3"})
print(f"\033[37m>\033[0m \033[36mBio \033[37m: {bio.string}\033[0m")
print()

try:
    upload = sp.find("img",{"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})["alt"]
    gv = sp.find("img",{"class":"tiktok-1itcwxg-ImgPoster e1yey0rl1"})["src"]
    view = sp.find("strong",{"class":"video-count tiktok-1p23b18-StrongVideoCount eor0hs42"})
    print(f"\033[37m>\033[0m \033[36mUpload Terakhir \033[37m: {upload}\033[0m")
    print()
    print(f"""\033[37m>\033[0m \033[36mLink Gambar video \033[37m: ↲
    
{gv}\033[0m""")
    print()
    print(f"\033[37m>\033[0m \033[36mViewers : {view.string} ↲\033[0m")
    print()
except Exception as e:
    sys.exit(">> Akun diprivasi <<\n")