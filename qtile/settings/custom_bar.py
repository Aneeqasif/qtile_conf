from libqtile import qtile, widget, bar
from libqtile.lazy import lazy
from .themes.fonts import font
from .themes.colors import colours
from qtile_extras import widget

bg = colours["bar_bg"]
widget_bg = colours["widget_bg"]

from .widgets_conf import *



padding = 10 
def get_widget_list():
    return [
        *left_side_padding(padding),
        my_current_screen(),        
        # my_text("", foreground="#C62A88" ,fontsize="26" ), #  
        *right_side_padding(padding),
        widget.Prompt(),
        *left_side_padding(padding),
        my_window_name(),
        # my_task(),
        in_line_sep(padding, widget_bg),
        my_layout_icon(),
        *full_padding(),
        my_group_box(),
        right_pad(),
        spacer(),
        sep(padding=0),
        spacer(),
        left_pad(),
        my_time(),
        my_date(),
        in_line_sep(padding, widget_bg),
        # my_text("墳"),
        # in_line_sep(5, widget_bg),
        # my_volume(),

        in_line_sep(5, widget_bg),
        ubattery(),
        in_line_sep(7, widget_bg),
        # my_battery_icon(background=widget_bg),
        my_extender(background=bg),

        *right_side_padding(padding)
           ]



def get_widget_list_primary():
    widgets = get_widget_list()
    widgets.insert(-7, my_systray())
    return widgets
        

def my_bar(is_primary):
    # widgets = get_widget_list()
    widgets = get_widget_list_primary() if is_primary else get_widget_list()
    return bar.Bar(
        widgets,
        28,
        opacity=1.0,
        margin=[5, 4, 0, 4],  # top right bottom  left
        background=colours["bar_bg"],
        border_color=colours["bar_bg"],
        border_width=[4, 5, 5, 5]  # top right bottom  left

    )
