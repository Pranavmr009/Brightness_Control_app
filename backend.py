import screen_brightness_control as sbc
import os


def brightness(percent, display):
    brightness = sbc.get_brightness()

    primary = sbc.get_brightness(display=0)
    secondary = sbc.get_brightness(display=1)

    monitor1 = f"{primary}%"
    monitor2 = f"{secondary}%"

    if display == 0:
        sbc.set_brightness(percent, display=0)

    elif display == 1:
        sbc.set_brightness(percent, display=1)

    else:
        pass


def enable_night_light():
    os.system('gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled true')


def disable_night_light():
    os.system('gsettings set org.gnome.settings-daemon.plugins.color night-light-enabled false')
