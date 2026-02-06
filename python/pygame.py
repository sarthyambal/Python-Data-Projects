import pygame
import time

def play_tum_tak():
    # Initialize pygame mixer
    pygame.mixer.init()
    
    try:
        # Load the song file (ensure the file is in the same directory)
        pygame.mixer.music.load('tum_tak.mp3')
        print("Playing: Tum Tak - Raanjhanaa")
        
        # Play the song
        pygame.mixer.music.play()
        
        # Keep the script running while the song plays
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    except pygame.error as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        # Stop on Ctrl+C
        pygame.mixer.music.stop()
        print("\nSong stopped.")

if __name__ == "__main__":
    # You need to have "tum_tak.mp3" in the same folder
    play_tum_tak()
