from libqtile.config import Key, Group, ScratchPad, DropDown, Match
from libqtile import qtile, hook
from libqtile.command import lazy
from .mykeys import mod, keys
alt = "mod1"
mod = "mod4"


# 򺊴󱙼󰽢


# group_labels = ["", "", "", "", "", "", "", "", "", "",]
# labels = ["", "", "", "", "", "", "", ""]
# labels = ["", "", "", "", "", "", "", ""]
# labels = ["", "", "", "", "", "", "", ""]
# labels = ["", "", "", "", "", "⬤", "", ""]
# labels = ["", "", "", "", "", "󰽢", "󰽢", "󰽢"]
mach = [Match(wm_class=["Navigator", "firefox"]), 
        Match(wm_class=["okular", "okular"]),
        "",
        "",
        "",
        "",
        "",
        "",
        Match(wm_class=["xterm"])]

labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# groups = [Group(name=str(i + 1), label=label, matches=matches) for i, (label,matches) in enumerate(zip(labels,mach))]
groups = [Group(name=str(i + 1), label=label) for i, label in enumerate(labels)]




for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

### Move to previous group with foucs on that window
        Key([mod], "i", lazy.screen.next_group(),
                desc="Switch to next group"),
        
        Key([mod], "u", lazy.screen.prev_group(),
                desc="Switch to previous group"),

        Key([mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),

    ])


#### SCRATCHPADS ####

groups.append(
        ScratchPad("scratchpad", [
            DropDown("term", "kitty", height=0.8),
            DropDown("filem", "pcmanfm-qt", height=0.8),
            DropDown("vol_con", "pavucontrol", x=0.45, height=0.5, width=0.5, on_focus_lost_hide="False"),
            
            ]),
       )


def getIndex(currentGroupName):
    for i in range(len(groups)):
        if groups[i].name == currentGroupName:
            return i
# def toPrevGroup(qtile):
#     currentGroup = qtile.currentGroup.name
#     i = getIndex(currentGroup)
#    lazy.currentWindow.togroup(groups[ (i - 1) % len(groups)].name)
# def toNextGroup(qtile):
#     currentGroup = qtile.currentGroup.name
#     i = getIndex(currentGroup)
#     lazy.currentWindow.togroup(groups[ (i + 1) % len(groups)].name)
#
def toNextGroup():
    # currentGroup = qtile.currentGroup.name
    
    lazy.window.togroup("6")


@lazy.window.function
def monocle(win):
    win.cmd_toggle_floating()
    if win.floating:
        win.cmd_center()

# include this in your 'keys' list
keys.append(Key([mod], "m", monocle))
# keys.append(Key([mod], "t", lazy.function(toPrevGroup)))
keys.append(Key([mod], "y", lazy.window.togroup("6",switch_group=True )))




