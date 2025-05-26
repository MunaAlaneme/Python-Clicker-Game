import pygame
import numpy as np
import scipy.signal

def resample_sound(sound, pitch_factor):
    # Extract raw sound buffer
    raw = pygame.sndarray.array(sound)
    
    # Get the current shape
    num_samples = raw.shape[0]

    # Calculate new length
    new_length = int(num_samples / pitch_factor)

    # Resample using scipy
    resampled = scipy.signal.resample(raw, new_length)

    # Convert to int16 for pygame compatibility
    resampled = resampled.astype(np.int16)

    # Convert back to a Sound object
    return pygame.sndarray.make_sound(resampled)

# --- Usage ---
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)

# Load original sound
original = pygame.mixer.Sound("./assets/audio/(radzlan - Miami Hotline Vol.3 (feat. Demonicity)) 673473_-Miami-Hotline--Vol3.wav")

# Resample (e.g., 1.5x pitch and speed)
new_sound = resample_sound(original, pitch_factor=1.5)

# Play new sound
new_sound.play()

# Keep program running while sound plays
pygame.time.wait(int(new_sound.get_length() * 1000))
pygame.quit()
