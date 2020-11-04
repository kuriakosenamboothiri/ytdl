from __future__ import unicode_literals
import youtube_dl
import os
location=input("Enter full download location")
if location == "":
  location = "/content/drive/"
os.chdir(location)
link = input("Enter Link : ")
ydl_opts = {
    
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
