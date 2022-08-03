# Imports {{{
from libqtile import widget,qtile, bar
from .themes.colors import colours
from .themes.fonts import font , font2
from libqtile.command import lazy
from qtile_extras import widget

# }}}

# variables {{{

bg = colours["widget_bg"]
fg = colours["widget_fg"]

# }}}

# decorations {{{

# from qtile_extras.widget.decorations import RectDecoration
# decor = {
#     "decorations": [
#         RectDecoration(colour="#600060", radius=10, filled=True, padding_y=5)
#     ],
#     "padding": 18,
# }
#
# widget.Clock(**decor),
#
# }}}

# current_screen & GroupBox {{{

def my_current_screen(background= bg):
    return widget.CurrentScreen(
        font= "Font Awesome 5 Pro",
        fontsize= font["fontsize"] + 6,
        active_text= "",
        inactive_text= "",
        background= background,
        active_color= colours["focused"],
        inactive_color= colours["active"]

    )


def my_group_box():
    return widget.GroupBox(
            background = bg,
            foreground = fg,
            this_current_screen_border = colours["focused"],
            active = colours["active"],
            inactive = colours["inactive"],
            center_aligned = False,
            highlight_method = "line", # Method of highlighting ('border', 'block', 'text', or 'line')
            rounded = True,
            font = "PragmataPro Bold Italic",
            disable_drag=True,
            urgent_text="#ff0000",
            fontsize = font["fontsize"] + 4,
    )

# }}}

# {{{ Layout_icon & Systray

def my_layout_icon():
    return widget.CurrentLayoutIcon(
        background=bg,
        mouse_callbakcs={"Button1": lazy.next_layout},
        scale=0.75
    )


# _____________________________________________________________________


def my_systray():
    return widget.Systray(
        background = bg,
        foreground = fg,
    )

# }}}

# Date & Time {{{

def my_time():
    return widget.Clock(
        background=bg,
        foreground=fg,
        format="  %I:%M %P",
        font = "Inter Medium",
        fontsize = 14,
        # **font
    )
def my_date():
    return widget.Clock(
        background=bg,
        foreground=fg,
        format="%a %d-%m",
        font = "Inter Medium",
        fontsize = 11,
        # **font
    )

# }}}

# my_text {{{
def my_text(text,fontsize='14',foreground=fg):
    return widget.TextBox(
        text=text,
        font='Material Design Icons',
        fontsize=fontsize,
        padding=0,
        background=bg,
        foreground=foreground
    )

# _____________________________________________________________________

# }}}

# my_battery_icon {{{

def my_battery_icon(background=bg):
    return  widget.BatteryIcon(
        theme_path="/home/aneeq/.config/qtile/battery_icons/", 
        background=bg,
        update_interval="10",
        notify_below="20",
        show_short_text=True
        )

    
# }}}

# my_window_name {{{

def my_window_name(pad=10):
    return widget.WindowName(
        **font,
        format='{name}',
        background=bg,
        # max_chars=22,
        foreground=fg,
        # font = "Inter",
        # fontsize = 13,
        # center_aligned=True,
        # padding=pad
    )

# }}}

# my_task_list {{{

def my_task_list(pad=10):
    return widget.TaskList(
        # **font,
        # format='{name}',
        background=bg,
        # max_chars=22,
        foreground=fg,
        # center_aligned=True,
        # padding=pad
    )

# }}}

# my_volume {{{

def my_volume():
    return widget.Volume(
        font = font["font"],
        fontsize = font["fontsize"],
        background = bg,
        foreground = fg,
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
    )

# }}}

# my_power_button {{{

def my_power_button():
    return widget.TextBox(
        text="",
        font=font["font"],
        fontsize=font["fontsize"] ,
        padding=0,
        background="#ff00ff",
        foreground="#00ffff",
        mouse_callbakcs={'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
    )

# }}}

# ubattery , cpu ,extender {{{

def ubattery(background=bg):    
    return widget.UPowerWidget( 
        background = background,
        battery_height=12,
        border_charge_colour='#86ffa2',
        fill_low="#aa2f3f"
            )


def my_cpu(background = bg):
    return widget.CPUGraph(
            background = background,
            )



extended_widgets =  [
            my_cpu(),
            ]


def my_extender(background=bg):
    return widget.WidgetBox(
    background=background,
    close_button_location="right",
    text_closed="",
    text_open="",
           
           widgets=extended_widgets)


# }}}

#    __padding__ {{{ 

pbg = colours["bar_bg"]
pfg = colours["widget_bg"]

def left_pad():
    return widget.TextBox(
        text='',
        fontsize='27',
        font='JetBrainsMono Nerd Font',
        padding=0,
        background=pbg,
        foreground=pfg
    )
def right_pad():
    return widget.TextBox(
        text='',
        fontsize='27',
        font='JetBrainsMono Nerd Font',
        padding=0,
        background=pbg,
        foreground=pfg
    )

def sep(padding,background=pbg):
    return widget.Sep(
        padding=padding,
        linewidth=0,
        background=pbg
    )

def spacer(length = bar.STRETCH):
    return widget.Spacer(length)

def in_line_sep(padding, new_bg):
    return widget.Sep(
        padding=padding,
        linewidth=0,
        background=new_bg
    )

def left_side_padding(padding):
    return [
        sep(padding),
        left_pad()
    ]
def right_side_padding(padding):
    return [
        right_pad(),
        sep(padding)
    ]
def full_padding(length = bar.STRETCH):
    return [
        right_pad(),
        spacer(length),
        left_pad()
    ]

# }}}
