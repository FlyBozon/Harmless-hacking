
import os
import platform
import ctypes
import subprocess
import sys

def set_wallpaper(image_path):
    system = platform.system()
    abs_path = os.path.abspath(image_path)

    if system == "Windows":
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, abs_path, 3)
        print(f"Wallpaper set on Windows: {abs_path}")

    elif system == "Linux":
        if "SUDO_USER" in os.environ:
            print("Do NOT run this script with sudo! Exiting.")
            sys.exit(1)

        desktop_env = os.environ.get('XDG_CURRENT_DESKTOP', "").lower()

        try:
            if "gnome" in desktop_env or "ubuntu" in desktop_env:
                subprocess.run([
                    "gsettings", "set", "org.gnome.desktop.background", "picture-options", "zoom"
                ], check=True)
                subprocess.run([
                    "gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{abs_path}"
                ], check=True)
                subprocess.run([
                    "dbus-send", "--session", "--dest=org.gnome.Shell", "--type=method_call",
                    "/org/gnome/Shell", "org.gnome.Shell.Eval",
                    'string:Main.panel.statusArea.dateMenu._clock.update();'
                ], check=True)
                print(f"Wallpaper set using gsettings for GNOME: {abs_path}")

            else:
                subprocess.run(["feh", "--bg-scale", abs_path], check=True)
                print(f"Wallpaper set using feh: {abs_path}")

        except subprocess.CalledProcessError:
            print("Failed to set wallpaper: gsettings or feh failed.")

    else:
        print(f"Setting wallpaper not supported on {system}")

if __name__ == "__main__":
    image_folder = "./img"
    image_filename = "download.jpeg"  #adjust to your image

    image_path = os.path.join(image_folder, image_filename)
    
    if os.path.exists(image_path):
        set_wallpaper(image_path)
    else:
        print(f"Image not found: {image_path}")

