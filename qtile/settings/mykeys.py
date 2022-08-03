
from libqtile.config import Key, KeyChord, Group
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

# terminal = "/home/aneeq/scripts/st"   #guess_terminal()
terminal = "kitty"   #guess_terminal()
keys=[]
alt = "mod1"
mod = "mod4"

# functions {{{

@lazy.window.function
def window_to_next_group(window):
    index = window.qtile.groups.index(window.group)
    index = (index + 1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name , switch_group=True )

@lazy.window.function
def window_to_prev_group(window):
    index = window.qtile.groups.index(window.group)
    index = (index + -1) % len(window.qtile.groups)
    window.cmd_togroup(window.qtile.groups[index].name , switch_group=True )


# Your keybinding would just be to `window_to_next_group`
# }}}


keys.extend( 
    [

####  __Window Controls {{{
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

# }}}

### __Column Layout Bindings {{{
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

# }}}

    #: {{{ __Scrathpads Bindings

    Key([mod], 'a', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], 'e', lazy.group['scratchpad'].dropdown_toggle("filem")),
    Key([mod, "control"], '1', lazy.group['scratchpad'].dropdown_toggle('vol_con')),
    Key([mod], "g", lazy.togroup()),
    #: }}}

#  __Custom KeyBinidings {{{
    Key([mod, alt], "l", lazy.spawn("xautolock -locknow"), desc="Lock Screen"),
    # Key([mod, alt], "l", lazy.spawn("i3lock-fancy-rapid 8 8"), desc="Lock Screen"),
    Key([mod], "w", lazy.spawn("jumpapp firefox"), desc="Launch firefox"),
    Key([mod], "b", lazy.spawn("jumpapp okular"), desc="Launch firefox"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "grave", lazy.next_layout(), desc="Toggle between layouts"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volin.sh dec &")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("volin.sh inc &")),
    Key([mod, "shift"], "a", lazy.window.toggle_floating(), desc="Spawn a command using a prompt widget"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui")),
    Key([mod], 'comma', lazy.next_screen(), desc='Next monitor'),
    
    Key([mod, "shift"], "o", window_to_prev_group , desc="window_to_prev_group"),

    Key([mod, "shift"], "p", window_to_next_group , desc="window_to_next_group"),



#: }}}

# key chords {{{
     KeyChord([mod], "z", [
            Key([], "x", lazy.spawn("xterm"))
        ]),

])

# }}}





