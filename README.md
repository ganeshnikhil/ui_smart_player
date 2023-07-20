# ui_smart_player

### Music Player

This project is a simple music player written in Python using the Pygame library. It allows you to play songs stored in a specified directory, keeps track of the number of times each song is played, and displays the remaining time of the currently playing song. The music player also provides options to scroll through the list of songs, pause/play the current song, and go back to previously played songs.

## Installation

1. Clone the repository:

```
git clone <repository_url>
cd <project_directory>
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Modify the `music_setting.json` file to set the path of your music directory and customize other settings according to your preferences.

```json
{
    "path": " ",
    "repeater": 0,
    "//": "possible value of repeater (0,-1)",
    "scroll_speed": 20,
    "scroll_offset": 0,
    "song_spacing": 29,
    "screen_length": 26,
    "//": "total height will song_spacing*screen_length",
    "screen_width": 640,
    "initial_color": "white",
    "final_color": "red"
}
```

2. Run the main script:

```bash
python main.py
```

## Functionality

- The music player reads the list of songs (in .mp3 and .wav formats) from the specified directory.
- It creates an empty JSON file named `data.json` to store the number of times each song is played.
- If the `data.json` file already exists, the program checks for any missing songs in the file and adds them with an initial weightage of 0.
- The user can click on a song to play it, and the player will keep track of the song's play count and update the JSON file accordingly.
- Songs are displayed on the screen, and the list can be scrolled up and down if there are more songs than can be displayed at once.
- The player shows a loading bar indicating the progress of the current song.
- The remaining time of the current song is displayed on the screen.

## Customization

You can customize various settings in the `music_setting.json` file:

- `"path"`: Specify the path of the directory containing your music files.
- `"repeater"`: Set the number of times a song should repeat after its completion. Use `0` for one-time play, `-1` for continuous repeat, and any positive integer to repeat the song the desired number of times.
- `"scroll_speed"`: Adjust the scrolling speed of the song list when there are more songs than can be displayed at once.
- `"scroll_offset"`: Set the initial scroll offset of the song list.
- `"song_spacing"`: Adjust the spacing between song names on the screen.
- `"screen_length"`: Set the number of songs visible on the screen at once.
- `"screen_width"`: Set the width of the display screen.
- `"initial_color"`: Set the initial color of the song names. Supported color names are specified in the `colors.json` file.
- `"final_color"`: Set the color of the song names when hovered over. Supported color names are specified in the `colors.json` file.


## Features 
- Automatically loads all the songs present in the specified directory with .mp3 or .wav extension.
- Keeps track of the play count for each song in a JSON file named data.json.
- Allows you to click on a song to play it and updates the play count.
- Supports basic music controls: play, pause, and skip.
- Displays the remaining time of the current song.
- Offers customizable settings to
- Bultin song library . preinstalled songs.
  
## Bulitin  songs library 
  **song list**
  
 - Memories - Maroon-5-320-(PagalWorld).mp3
 - chill-lofi-song-8444.mp3
 - night-city-drive-loopable-crime-thriller-mystery-mood-7584.mp3
 - cheerful-cinematic-song-without-solo-guitar-10709.mp3
 - komm-lieber-mai-und-mache-overbeck-mozart-come-dear-may-and-make-3468.mp3
 - 99a6ace6a083234b2cdae1b178eed860.wav
 - Womanizer - Britney-Spears(PagalWorld).mp3
 - Cupid.mp3
 - mozart-turkish-march-music-127960.mp3
 - calm-documentary-118669.mp3
 - dead-by-daylight-10243.mp3
 - Dark-Horse - Katy-Perry-320(PagalWorld).mp3
 - love-song-10539.mp3
 - nature-song-116650.mp3
 - Trampoline - Zayn-Malik(PagalWorld).mp3
 - Im-Faded_320(PagalWorld).mp3
 - Halsey_-_Colours.mp3
 - oh-christmas-tree-dj-williams-129977.mp3
 - Often-Slowed-Reverb_320(PagalWorld).mp3
 - Besharam-Rang-Kaha-Dekha_320(PagalWorld).mp3
 - Some-Time-I-Wanna-Thinks-About-You_320(PagalWorld).mp3
 - Lo-Safar-Shuru-Ho-Gaya_320(PagalWorld).mp3
 - let-it-go-12279.mp3
 - Kabhi-Kabhi-Aditi-Zindagi(PagalWorld).mp3
 - Bloody Mary New Song Download Mp3(SongsZilla.Net).mp3
 - o-come-o-come-emmanuel-11563.mp3
---
[**Screeeshot of GUI**] (https://github.com/ganeshnikhil/ui_smart_player/blob/main/Screenshot%202023-07-20%20at%205.55.33%20PM.png)

This music player project provides a basic framework to get started with creating your own music player in Python. If you have any further questions or need assistance, don't hesitate to ask!
