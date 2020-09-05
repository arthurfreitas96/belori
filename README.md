# belori
Special thanks to Lucas Lugão Guimarães

This is a simple application that uses youtube-dl to download songs from YouTube to your computer.

Use the 'SearchQuery.txt' file in the 'config' folder to write the names of your favorite songs according to the following format:

Playlist name here, in the first line
#
first song here
second here
third here
and so on

Don't worry about fancy writing the song names. Write them as if you were searching on YouTube.

After finishing with the 'SearchQuery.txt' file, from terminal, run 'python3 downloader.py' to start downloading the playlist. You can follow the running process via terminal outputs.

The songs will be saved in a folder named after your playlist choosen name. This folder also includes a .m3u file with the same name and the song names are stored inside it following the order requested in the 'SearchQuery.txt' file.

You can create new playlists simple by requesting songs to a nonexistent playlist name. Likewise, you can add songs to a playlist by requesting songs to a preexistent playlist name. All your playlists are stored inside a 'Playlists' folder.

Dependences:
python3
youtube-dl
