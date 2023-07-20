import os
import json
import pygame
import audioread

#Path of all important variables
with open('music_setting.json', 'r') as f:
    data = json.load(f)

path = data["path"]

#Get the names of all files in the directory
files = os.listdir(path)

# Get all song file names that end with .wav or .mp3
songs = [song for song in files if song.endswith('.mp3') or song.endswith('.wav')]

# Create an empty JSON file with song names as keys and 
# initial weightage  as 0
def empty_json(songs):
    dic = {}
    for song in songs:
        dic[song] = 0
    json_object = json.dumps(dic, indent=4)
    with open("data.json", "w") as outfile:
        outfile.write(json_object)
        
 # Check if any songs are missing in the existing JSON file and add that song 
 # and assign value 0 to it.
def missing_json(songs):
    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
    if len(data.keys()) != len(songs):
        for song in list(data.keys()):
            if song not in songs:
                del data[song]
                
        for song in songs:
            if song not in data:
                data[song]=0 
        with open("data.json", "w") as outfile:
            json.dump(data, outfile,indent=4)

# Check if the JSON file is empty
if os.path.isfile("data.json") == False:
    empty_json(songs)
# If songs are missing in the JSON file
else:
    missing_json(songs)

# load the stored song in json file 
filename = open('data.json', 'r')
data_stored = json.load(filename)
filename.close()
all_played_count = []
for i, song in enumerate(data_stored.keys()):
    # Load the JSON data into a list
    all_played_count.append([song, data_stored[song], i])

# Sort the all_played_count 2D list based on the number of hits in descending order
new_played_count = sorted(all_played_count, key=lambda x:x[1], reverse=True)

# Initialize the song_list to empty
song_list = []
for i in range(len(new_played_count)):
    # Append the song name and song index to the list for future use
    song_list.append([new_played_count[i][0], new_played_count[i][2]])

# Generate the song run time
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{round(hour)}:{round(minutes)}:{round(seconds)}"
# the calculate the song duration of song file in seconds 
def get_song_duration(file_path):
    with audioread.audio_open(file_path) as audio:
        duration = audio.duration
    return duration

   
# Initialize Pygame event to check for song end.
pygame.init()
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

# Set the repeater variable .
# loop the song according to you repeater value.
repeater = data['repeater']
    
# Play a song from the given path
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Create a font object for rendering text
font = pygame.font.Font(None, 24)

# get the colors of text stored in colors json file 
with open('colors.json','r') as f:
    all_colors=json.load(f)


intial_color=all_colors[data['intial_color']] # white
final_color=all_colors[data['final_color']] #red

# check if input colors from setting  is not in color.json file 
# intialize the variable to white and red 
if data['intial_color'] not in all_colors:
    intial_color=all_colors['white']
if data['final_color'] not in all_colors:
    final_color=all_colors['red']
    
# Render the song names as text objects
song_texts = [font.render(song[0], True, intial_color) for song in song_list]

# Create rectangles for the song texts
song_rects = [song.get_rect() for song in song_texts]

# Set the spacing between song texts
song_spacing = data["song_spacing"]
screen_length = data["screen_length"]

# Calculate the screen height based on the number of songs
screen_height = screen_length * song_spacing

# Create the game screen
screen_width = data["screen_width"]
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Set the background
background_image = pygame.image.load("hello.jpg")
background_width, background_height = background_image.get_size()

# Calculate the scale factor to fit the image within the screen
scale_factor = min(screen_width / background_width, screen_height / background_height)

# Scale the background image
scaled_width = int(background_width * scale_factor)
scaled_height = int(background_height * scale_factor)
background_image = pygame.transform.scale(background_image, (scaled_width, scaled_height))

# Calculate the position to center the image on the screen
x = (screen_width - scaled_width) // 2
y = (screen_height - scaled_height) // 2
visible_song_count = screen_height // song_spacing

# Initialize the list to keep track of played songs
intial_played_index = []

# Define the initial and final song indices.
intial_index = -1
final_index = -1

# Define the scrolling variables
scroll_speed = data["scroll_speed"]
scroll_offset = data["scroll_offset"]

# Variable to pause and play the song
pause_play = 0

# Loading bar variables
loading_bar_width = 0
loading_bar_max_width = screen_width
loading_bar_height = 10
loading_bar_color = (0, 255, 0)

# Check if scrolling is possible
def check_scroll():
    if len(song_list) > visible_song_count:
        return True
    return False

# calculate the timing of played song.
def calculate_time(current_time, song_length):
    remaining_time = song_length - current_time
    return convert(remaining_time)

# Function to manage song playback
def song_mangaed_play(i):
    global intial_index
    global final_index

    # Play the selected song
    play_song(path + song_list[i][0])
    print("Clicked on song:", song_list[i][0])
    intial_index = i
    # Swap the initial and final indices
    intial_index, final_index = final_index, intial_index

    # Set the color of the final song text to green
    song_texts[final_index] = font.render(song_list[final_index][0], True, final_color)

    # Set the color of the initial song text to white if it is not the final song
    if intial_index != final_index:
        song_texts[intial_index] = font.render(song_list[intial_index][0], True, intial_color)

# Update the weightage of a song
def song_update(i):
    with open("data.json", 'r') as f:
        json_object = json.load(f)
    print(json_object[song_list[i][0]])
    json_object[song_list[i][0]] += 1
    with open('data.json', 'w') as file_update:
        json_updated = json.dump(json_object, file_update, indent=4)

# Main game loop
running = True
remaining_time = "00:00:00"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # play the song from the history 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if len(intial_played_index) > 0:
                    song_mangaed_play(intial_played_index[-1])
                    print(intial_played_index)
                    intial_played_index.pop()
            # pause play logic      
            elif event.key == pygame.K_RETURN:
                pause_play += 1
                if pause_play % 2 == 0:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            # scroll the song    
            elif event.key == pygame.K_UP and check_scroll() == True:
                scroll_offset += scroll_speed
            elif event.key == pygame.K_DOWN and check_scroll() == True:
                scroll_offset -= scroll_speed
        # if song clicked playe that son g
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, rect in enumerate(song_rects):
                    if rect.collidepoint(event.pos):
                        song_mangaed_play(i)
                        song_update(i)
                        # If the played song is played again, bring it to the top and remove its initial position
                        if intial_index in intial_played_index:
                            if intial_index != -1:
                                intial_played_index.remove(intial_index)
                                intial_played_index.append(intial_index)
                        else:
                            if intial_index != -1:
                                intial_played_index.append(intial_index)
        # song end event when song end new song is loaded automatically.                      
        elif event.type == SONG_END:
            if repeater == 0:
                if final_index < len(song_list)-1:
                    new_index = final_index + 1
                    song_mangaed_play(new_index)
                else:
                    new_index = 0
                    song_mangaed_play(new_index)
            else:
                # if repeater is -1 play continuosly 
                if repeater==-1:
                    song_mangaed_play(final_index)
                # play the song as no of  time you desire
                else:
                    repeater=repeater-1
                    song_mangaed_play(final_index)
                #remaining_time="00:00:00"
                
            if intial_index not in intial_played_index:
                intial_played_index.append(intial_index)
        # change the color of text when pointer hover over it
        elif event.type == pygame.MOUSEMOTION:
            for i, rect in enumerate(song_rects):
                if rect.collidepoint(event.pos):
                    song_texts[i] = font.render(song_list[i][0], True, final_color)
                else:
                    if i != final_index:
                        song_texts[i] = font.render(song_list[i][0], True, intial_color)

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the background image on the screen
    screen.blit(background_image, (x, y))

    # Update the loading bar
    if pygame.mixer.music.get_busy():
        song_length=get_song_duration(path+song_list[final_index][0])
        current_time = pygame.mixer.music.get_pos() / 1000
        loading_bar_width = min((current_time / song_length) * loading_bar_max_width, loading_bar_max_width)
        # calculate the remaining time.
        remaining_time = calculate_time(current_time, song_length)
        
    # Render and position the song texts on the screen with scrolling
    for i, (text, rect) in enumerate(zip(song_texts, song_rects)):
        rect.topleft = (20, i * song_spacing + scroll_offset)
        if rect.bottom >= 0 and rect.top <= screen_height:
            screen.blit(text, rect)

    # Draw the loading bar
    pygame.draw.rect(screen, loading_bar_color, (0, screen_height - loading_bar_height, loading_bar_width, loading_bar_height))
    
    # Render the timer display
    timer_text = font.render(remaining_time, True, (255, 255, 255))
    timer_rect = timer_text.get_rect()
    timer_rect.bottomright = (screen_width - 20, screen_height - 20)
    screen.blit(timer_text, timer_rect)
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
print(intial_played_index)

# these are coustmizable variables of these program it is stored in music_setting.json file 
# "path":"/Users/kartiksingh/Downloads/songs/",
# "repeater":0,
# "//":"possible value of repeater (0,-1)",
# "scroll_speed":20,
# "scroll_offset":0,
# "song_spacing":29,
# "screen_length":26,
# "//":"total height will song_spacing*screen_length",
# "screen_width":640,
# "intial_color":"white",
#"final_color":"red"
