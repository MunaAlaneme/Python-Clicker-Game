import librosa
import numpy as np
import sounddevice as sd
import threading
import tkinter as tk
from tkinter import ttk
from queue import Queue
import time

# Load audio file (mp3, wav, etc.)
#audio_path = "./assets/audio/Kevin MacLeod - Hep Cats.mp3"
audio_path = "./assets/audio/Move Forward 111bpm FULL MIX.wav"
y, sr = librosa.load(audio_path, sr=None)

# Playback controls
playback_rate = [1.0]
playing = [True]

chunk_duration = 1/120  # seconds, if put at 1/4410, bitcrush
chunk_samples = int(sr * chunk_duration)
max_queue_size = 15 #if put at 100, bitcrush also
audio_queue = Queue(maxsize=max_queue_size)

def producer_thread():
    start = 0
    while start < len(y) and playing[0]:
        if audio_queue.full():
            time.sleep(0.01)
            continue
        end = start + int(chunk_samples/playback_rate[0])
        chunk = y[start:end]

        # Zero-pad input chunk to fixed length
        chunk = librosa.util.fix_length(chunk, size=int(chunk_samples/playback_rate[0]))

        # Resample based on playback rate
        rate = playback_rate[0]
        new_sr = int(sr * rate)
        resampled = librosa.resample(chunk, orig_sr=sr, target_sr=new_sr)

        # Fix output length to constant size (based on original sample rate)
        target_output_len = chunk_samples
        resampled = librosa.util.fix_length(resampled, size=target_output_len)

        # Normalize safely
        max_val = np.max(np.abs(resampled))
        if max_val > 0:
            resampled = resampled / max_val

        resampled = np.clip(resampled, -1.0, 1.0)

        audio_queue.put(resampled.astype(np.float32))
        #start += int(chunk_samples/playback_rate[0])
        start += int(chunk_samples/1)

def audio_callback(outdata, frames, time_info, status):
    if not audio_queue.empty():
        chunk = audio_queue.get()
        outdata[:] = chunk.reshape(-1, 1)
    else:
        outdata.fill(0)  # silence if buffer underrun

def update_rate(val):
    playback_rate[0] = .5**float(val)

def update_gui():
    if y is not None:
        fill = int((audio_queue.qsize() / max_queue_size) * 100)
        buffer_bar['value'] = fill
    if playing[0]:
        root.after(100, update_gui)

# GUI Setup
root = tk.Tk()
root.title("Smooth Audio Player with Pitch & Speed Control")

ttk.Label(root, text="Playback Rate (Pitch & Speed):").pack(pady=5)
slider = ttk.Scale(root, from_=-3, to=3, value=0, orient="horizontal", command=update_rate)
slider.pack(fill='x', padx=10)

ttk.Label(root, text="Buffer Fill:").pack(pady=5)
buffer_bar = ttk.Progressbar(root, length=200, mode='determinate')
buffer_bar.pack(fill='x', padx=10, pady=(0, 10))

ttk.Button(root, text="Stop", command=lambda: (playing.__setitem__(0, False), root.destroy())).pack(pady=10)

# Start producer thread
threading.Thread(target=producer_thread, daemon=True).start()

# Start audio stream
stream = sd.OutputStream(channels=1, samplerate=sr, dtype='float32',
                         callback=audio_callback, blocksize=chunk_samples)
stream.start()

update_gui()
root.mainloop()

# Cleanup on exit
playing[0] = False
stream.stop()
stream.close()