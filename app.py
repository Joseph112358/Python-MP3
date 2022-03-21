from tkinter import *
import pygame
from tkinter import filedialog

# Research mp3, wav and ogg files

root = Tk()
root.title('MP3 Player')
root.iconbitmap('S:/Downloads/GenZ_WWIII.png')
root.geometry("500x360")

# Initialize Pygame Mixer.
pygame.mixer.init()

#file dialouge
# Add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='S:\Python\MP3_Player\tracks', title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #Take out directory info
    song = song.replace("S:/Python/MP3_Player/tracks/","")
    #song = song.replace(".mp3","")
    song_box.insert(END, song)
#Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'S:/Python/MP3_Player/tracks/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Create Playlist Box.
song_box = Listbox(root, bg="black", fg ="green",width=60,selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)

# Create Player controls
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

#Create player control frame
controls_frame = Frame(root)
controls_frame.pack()

#Create player control buttons
back_button = Button(controls_frame, image=back_btn_img,borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img,borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img,borderwidth=0,command=play)
pause_button = Button(controls_frame, image=pause_btn_img,borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img,borderwidth=0,command=stop)

back_button.grid(row=0,column=0,padx=10)
forward_button.grid(row=0,column=1,padx=10)
play_button.grid(row=0,column=2,padx=10)
pause_button.grid(row=0,column=3,padx=10)
stop_button.grid(row=0,column=4,padx=10)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song to playlist",command=add_song)



root.mainloop()
