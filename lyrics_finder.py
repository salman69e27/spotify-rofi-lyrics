#!/usr/bin/env python

import subprocess
import os
import sys
from dotenv import load_dotenv
import lyricsgenius

# load genius api access token
load_dotenv()
TOKEN = os.getenv('ACCESS_TOKEN')

path_to_lyrics = format(os.path.join(sys.path[0], 'cur_lyrics'))
path_to_status = '"{}"'.format(os.path.join(sys.path[0], 'spotify_status.py'))
get_status_command = 'python3 {} -t 1000'.format(path_to_status)

# get current song name
artist_plus_song = subprocess.check_output(get_status_command, shell=True).decode('utf-8')
# if empty then exit
if artist_plus_song == '\n':
    with open(path_to_lyrics, 'w+') as lyrics_file:
        lyrics_file.write("Nosing playing (pun intended)")
    exit()

# convert binary string to utf-8 and extract artist and song
artist_plus_song = artist_plus_song[:-1]
artist, song = artist_plus_song.split(':')
song_name = song[1:]

genius = lyricsgenius.Genius(TOKEN)
song = genius.search_song(song_name, artist)

# write lyrics to file
with open(path_to_lyrics, 'w+') as lyrics_file:
    if song is None:
        lyrics_file.write('Lyrics not found')
    else:
        lyrics_file.write(song.lyrics)
