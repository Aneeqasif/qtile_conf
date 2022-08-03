
import os
import socket
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.extension import window_list as WList
from settings.mykeys import keys
from settings.mygroups import *
from settings.custom_bar import my_bar
from settings.myscreen import screens
from settings.themes.colors import colours
import re
from libqtile.log_utils import logger

# from libqtile.extension.dmenu import DmenuRun
# from libqtile.extension.window_list import WindowList

alt = "mod1"
mod = "mod4"
terminal = "kitty"   #guess_terminal()

follow_mouse_focus = "False"
bring_front_click = "True"


# def init_layout_theme():
#     return {"margin":4,
#             "border_width":2,
#             "border_focus": "#6080a4",
#             "border_normal": "#2a303b"
#             }
# layout_theme = init_layout_theme()
layout_theme = {"margin":4,
            "border_width":2,
            "border_focus": "#6080a4",
            "border_normal": "#37373d"
            }


layouts = [
    layout.Columns(**layout_theme),
    # layout.MonadTall(**layout_theme),
    layout.Tile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),

    # layout.MonadWide(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.Floating(border_focus="#61b9c5", border_width=2),
    layout.TreeTab(
            font="Ubuntu",
            fontsize=12,
            # sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
            section_fontsize=10,
            border_width=2,
            bg_color="#1c1f24",
            active_bg=colours["focused"],
            active_fg="#000000",
            inactive_bg="#8498a8",
            inactive_fg="#1c1f24",
            padding_left=0,
            padding_x=0,
            padding_y=5,
            section_top=10,
            section_bottom=20,
            level_shift=8,
            vspace=3,
            panel_width=200
        ), 
]

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            # ["#060d16", "#2F343F"], # color 1 blacker
            # ["#2F343F", "#2F343F"], # color 1
            ["#1e222a", "#1e222a"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()

# keys.append(Key([mod], 'p', lazy.run_extension(DmenuRun(
#         font="TerminessTTF Nerd Font",
#         fontsize="10",
#         dmenu_command="dmenu_run",
#         dmenu_prompt=" ",
#         dmenu_height=10,
#         dmenu_lines=15,
#         # background=gruvbox['bg'],
#         # foreground=gruvbox['fg'],
#         # selected_foreground=gruvbox['dark-blue'],
#         # selected_background=gruvbox['bg'],
#     ))))
# keys.append(Key([mod, "shift"], 'w', lazy.run_extension(WindowList(
#         all_groups=True,
#         # font="TerminessTTF Nerd Font",
#         fontsize="13",
#         dmenu_prompt=" ",
#         dmenu_height=10,
#         # dmenu_lines=15,
#         # background=gruvbox['bg'],
#         # foreground=gruvbox['fg'],
#         # selected_foreground=gruvbox['dark-blue'],
#         # selected_background=gruvbox['bg'],
#     )))
#     )



widget_defaults = dict(
    font="Inter",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# def init_widgets_list():
#     # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
#     widgets_list = [
#                widget.GroupBox(font="JetBrainsMono Nerd Font",
#                         fontsize = 16,
#                         margin_y = 3,
#                         border= colors[4],
#                         margin_x = 0,
#                         padding_y = 6,
#                         padding_x = 3,
#                         borderwidth = 1,
#                         disable_drag = True,
#                         active = colors[5],
#                         inactive = colors[9],
#                         rounded = False,
#                         highlight_method = "text",
#                         this_current_screen_border = colors[8],
#                         foreground = colors[2],
#                         background = colors[1]
#                         ),
#                widget.WindowName(),
#
#                widget.Clock(
#                         foreground = colors[5],
#                         background = colors[1],
#                         fontsize = 12,
#                         format="%Y-%m-%d %H:%M"
#                         ),
#                widget.Systray(
#                         background=colors[1],
#                         icon_size=20,
#                         padding = 4
#                         ),
#               ]
#     return widgets_list
#
# widgets_list = init_widgets_list()
#
#

# def init_screens():
#     return [Screen(top=bar.Bar(widgets=widgets_list, size=27, opacity=0.8)),  ]
#
# screens = init_screens()
#



mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button3", lazy.window.bring_to_front()),
]



dgroups_key_binder = None
dgroups_app_rules = []  # type: list
cursor_warp = False
floating_layout = layout.Floating(border_focus="#57718d", border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="qlipper"), 
        Match(title="pinentry"),  # GPG key password entry
    ]
)
#


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"

@hook.subscribe.client_new
def client_new(client):
    logger.warning(client)
    if client_check('firefox', client):
        client.togroup("1", switch_group=True)
    elif client_check('okular', client):
        client.togroup("2", switch_group=True)

def client_check(new_window, client):
    check = bool(re.search(new_window, client.name, re.IGNORECASE))
    return check


