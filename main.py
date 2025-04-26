import ctypes
import os

def set_wallpaper_windows(image_path):
    # Convert path to absolute and handle backslashes
    abs_path = os.path.abspath(image_path)
    
    # SPI_SETDESKWALLPAPER = 20
    # Update the user's wallpaper
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

# Example usage
set_wallpaper_windows("download.jpg")
