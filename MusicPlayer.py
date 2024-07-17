import tkinter as tk
from tkinter import Menu,filedialog
import pygame 
import os

pygame.mixer.init()


def add_song():
    song_paths = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    if song_paths:
        for song_path in song_paths:
            song_name = os.path.basename(song_path)
            playlist.insert(tk.END, song_name)
            songs.append(song_path)

def delete_song():
    selected_song_index = playlist.curselection()
    if selected_song_index:
        playlist.delete(selected_song_index)
        del songs[selected_song_index[0]]

def play_song():
    if playlist.curselection():
        selected_song_index = playlist.curselection()[0]
        selected_song = songs[selected_song_index]
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play(loops=0)

def pause_song():
    pygame.mixer.music.pause()

def stop_song():
    pygame.mixer.music.stop() 

def resume_song():
    pygame.mixer.music.unpause()    

def previous_song():
    selected_song_index = playlist.curselection()
    if selected_song_index:
        new_index = selected_song_index[0] - 1
        if new_index >= 0:
            playlist.select_clear(selected_song_index)
            playlist.select_set(new_index)
            play_song()

def next_song():
    selected_song_index = playlist.curselection()
    if selected_song_index:
        new_index = selected_song_index[0] + 1
        if new_index < len(songs):
            playlist.select_clear(selected_song_index)
            playlist.select_set(new_index)
            play_song()           

# Create the main window
root = tk.Tk()
root.title("Music Player")
root.geometry("800x600")
root.resizable(False,False)

# List to store songs
songs = []


# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Song", command=add_song)
file_menu.add_command(label="Delete Song", command=delete_song)

playlist =tk.Listbox(bg='black',fg='white',selectmode=tk.SINGLE,selectbackground='light blue',font=("Helvetica", 12),width=100,height=20)
playlist.pack(pady=20,padx=10)

# Create a frame for control buttons
control_frame = tk.Frame(root, bg="#2d2d2d")
control_frame.place(relx=0.5, rely=0.8, anchor="center")

# Add buttons for Play, Pause, Stop, Previous, and Next
play_button = tk.Button(
    control_frame, text="Play", command=play_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
play_button.grid(row=0, column=0, padx=10)

pause_button = tk.Button(
    control_frame, text="Pause", command=pause_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
pause_button.grid(row=0, column=1, padx=10)


resume_button = tk.Button(
    control_frame, text="Resume", command=resume_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
resume_button.grid(row=0, column=2, padx=10)

stop_button = tk.Button(
    control_frame, text="Stop", command=stop_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
stop_button.grid(row=0, column=3, padx=10)

prev_button = tk.Button(
    control_frame, text="Previous", command=previous_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
prev_button.grid(row=0, column=4, padx=10)

next_button = tk.Button(
    control_frame, text="Next", command=next_song, width=10, 
    height=2, bg="#1db954", fg="white", font=("Helvetica", 12, "bold"), 
    relief="flat"
)
next_button.grid(row=0, column=5, padx=10)

root.mainloop()
