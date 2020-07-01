
# spotify-rofi-lyrics
Show lyrics for the currently playing Spotify song using Rofi.

## Requirements 

 - Python 3.x with the following libraries:
	 - dotenv (`pip install python-dotenv`)
	 - lyricsgenius (`pip install lyricsgenius`)
 - Rofi
## Setup
After cloning the repo you need to make an api client and get an access token from [genius](https://genius.com/api-clients). Save the access token in a file named .env in the repo directory with the following command

    echo ACCESS_TOKEN=your_access_token > .env
## Usage
Launch the script `song_switch_listener.py` to trigger the script to get the lyrics and save it whenever the song changes. To show the lyrics of the current song launch the script `launch.sh` with `bash launch.sh`.

![Preview](https://github.com/salman69e27/spotify-rofi-lyrics/blob/master/preview.png)

You can add it to your polybar with the following module

    [module/spotify_lyrics]
	type = custom/text
	content = 
	click-left = bash path/to/launch.sh
## Acknowledgment  
The theme and colors are based on a rofi mpd widget by [Aditya Shakya](github.com/adi1090x) (with very few modifications). 
The `spotify_status.py` script is by [Dieter](github.com/dietervanhoof).
