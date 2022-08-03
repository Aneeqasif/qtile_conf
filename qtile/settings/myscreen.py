from libqtile import bar
from libqtile.log_utils import logger
import screeninfo

# Configure Screens
from libqtile.config import Screen
from .custom_bar import my_bar


# config = {
#     'wallpaper': '~/.config/qtile/wallpapers/mob_city.png',
#     'wallpaper_mode': 'fill',
# }

# screens = [
#     Screen(
#         # **config, 
#         top=my_bar(), 
#         # right=bar.Gap(8),
#     ), 
#     # for screen in screeninfo.get_monitors()
#     Screen(
#         top=my_bar(), 
#     ) 
# ]
#
screens = [
    Screen(
        top=my_bar(screen.is_primary), 

    ) 
    for screen in screeninfo.get_monitors()
]
