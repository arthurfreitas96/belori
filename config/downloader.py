from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import os

with open("SearchQuery.txt") as f1:
    SQcontent = f1.read().splitlines()

def AutoSearch(textToSearch):
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")
	vid = soup.find(attrs={'class':'yt-uix-tile-link'})
	with open('Links.txt', 'a') as f2:
		f2.write('https://www.youtube.com' + vid['href'] + '\n')

Playlist_name = SQcontent[0]

for query in SQcontent[2:]:
	AutoSearch(query)

with open("Links.txt") as f2:
	LKcontent = f2.read().splitlines()

os.chdir("..")

if((os.path.isdir("./Playlists") == 0)):
	os.system("mkdir Playlists")

os.chdir("./Playlists")

if((os.path.isdir("./" + Playlist_name) == 0)):
	os.system("mkdir " + Playlist_name)

os.chdir("./" + Playlist_name)

Playlist_name_m3u = Playlist_name + ".m3u"

with open(Playlist_name_m3u, 'a') as f3:
	for link in LKcontent:
		os.system("youtube-dl --extract-audio --audio-format mp3 " + link)
		files = sorted(os.listdir("./"), key=os.path.getctime)
		newest = files[-1]
		f3.write(newest + "\n\n")

os.chdir("..")

os.chdir("..")

os.chdir("./config")

os.system("rm -f Links.txt")

open('SearchQuery.txt', 'w').close()
