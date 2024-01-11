'''
Simple Youtube Downloader
'''

# import the needed packages
from pytube import YouTube
from sys import argv


url = input("Enter a YouTube link: ")
# url = argv[0]
yt = YouTube(url)

# Print the title to know if it's the right one
print("Title:", yt.title)

# get the video thumbnail
print("Image: ", yt.thumbnail_url)

# Check how many views
print("Views:", yt.views)

# set the video into the highest resolution
yd = yt.streams.get_highest_resolution()

# download the video then set the directory address to where it should be saved
yd.download("/Users/agcdtmr/Desktop/")
print("Successfully Downloaded!!")




