import subprocess
import os
import sys
from time import sleep

path_to_lyrics_finder = '"{}"'.format(os.path.join(sys.path[0], 'lyrics_finder.py'))
path_to_status = '"{}"'.format(os.path.join(sys.path[0], 'spotify_status.py'))
get_status_command = 'python3 {} -t 1000'.format(path_to_status)
find_lyrics_command = 'python3 ' + path_to_lyrics_finder
try:
    previous_song = ''
    while True:
        cur_song = subprocess.check_output(get_status_command, shell=True)
        if previous_song != cur_song:
            subprocess.call(find_lyrics_command, shell=True)
        previous_song = cur_song
        sleep(2)
except Exception as ex:
    os.system('notify-send "Problem with song_switch_listener.py. exiting.."')
    exit()
