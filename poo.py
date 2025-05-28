#./assets/audio/(radzlan - Miami Hotline Vol.3 (feat. Demonicity)) 673473_-Miami-Hotline--Vol3.mp3
import tkinter as tk
from tkinter import filedialog
import pygame
from pydub import AudioSegment
import numpy as np
from scipy.signal import resample
import threading
import time

# Init Pygame
sample_rate = 44100
pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

# Globals
audio_data = None
playing = False
start_frame = 0
frame_count = int(sample_rate * 0.1)  # smaller chunks for smoother updates
semitone_ratio = 2 ** (1 / 12)

# Load audio
def load_audio():
    global audio_data, start_frame
    file_path = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
    if not file_path:
        return
    audio = AudioSegment.from_file(file_path).set_channels(1).set_frame_rate(sample_rate)
    raw = np.array(audio.get_array_of_samples()).astype(np.float32)
    audio_data = raw
    start_frame = 0
    status_label.config(text=f"Loaded: {file_path.split('/')[-1]}")
    start_playback()

# Resample chunk with pitch shift
def resample_audio(data, pitch_factor):
    new_len = int(len(data) / pitch_factor)
    return resample(data, new_len)

# Start playback
def start_playback():
    global playing
    if audio_data is None:
        status_label.config(text="No audio loaded.")
        return

    if not playing:
        playing = True
        threading.Thread(target=play_loop, daemon=True).start()

# Stop playback
def stop_audio():
    global playing
    playing = False
    pygame.mixer.stop()

# Main loop
def play_loop():
    global start_frame
    while playing and start_frame < len(audio_data):
        semitone_step = semitone_slider.get()
        pitch_factor = 2 ** (semitone_step / 12)

        chunk = audio_data[start_frame:start_frame + frame_count]
        if len(chunk) == 0:
            break

        # Resample for pitch
        pitched = resample_audio(chunk, 1 / pitch_factor)
        pitched = np.clip(pitched, -32768, 32767).astype(np.int16)

        sound = pygame.mixer.Sound(buffer=pitched.tobytes())
        sound.play()

        time.sleep(len(pitched) / sample_rate)
        start_frame += frame_count

    playing = False

# GUI
root = tk.Tk()
root.title("Live Pitch Shift Player")

load_btn = tk.Button(root, text="Load Audio", command=load_audio)
load_btn.pack()

stop_btn = tk.Button(root, text="Stop", command=stop_audio)
stop_btn.pack()

semitone_slider = tk.Scale(root, from_=-12, to=12, orient=tk.HORIZONTAL, label="Semitone Shift")
semitone_slider.pack()

status_label = tk.Label(root, text="No audio loaded.")
status_label.pack()

root.mainloop()
