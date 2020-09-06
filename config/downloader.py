import os

with open("SearchQuery.txt") as f1:
    SQcontent = f1.read().splitlines()

Playlist_name = SQcontent[0]

os.chdir("..")

if((os.path.isdir("./Playlists") == 0)):
	os.system("mkdir Playlists")

os.chdir("./Playlists")

if((os.path.isdir("./" + "\"" + Playlist_name + "\"") == 0)):
	os.system("mkdir " + "\"" + Playlist_name + "\"")

os.chdir("./" + Playlist_name)

Playlist_name_m3u = Playlist_name + ".m3u"

with open(Playlist_name_m3u, 'a') as f2:
	for query in SQcontent[2:]:
		os.system("youtube-dl --extract-audio --audio-format mp3 \"ytsearch1:" + query + "\"")
		files = sorted(os.listdir("./"), key=os.path.getctime)
		newest = files[-1]
		f2.write(newest + "\n\n")

os.chdir("..")

os.chdir("..")

os.chdir("./config")

open('SearchQuery.txt', 'w').close()
