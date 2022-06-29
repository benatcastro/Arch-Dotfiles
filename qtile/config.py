from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
from spotify import Spotify
import os


mod = "mod1"
terminal = guess_terminal()

keys = [
    #Switch Monitors
    Key([mod], "Tab", lazy.next_screen()),
    #Spotify Keybindings
    Key([], "XF86AudioPlay",
    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2    " "org.mpris.MediaPlayer2.Player.PlayPause"),
    desc='Audio play'),

    Key([], "XF86AudioNext",
    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Next"),
    desc='Audio next'),

    Key([mod], "XF86AudioNext",
    lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify " "/org/mpris/MediaPlayer2 " "org.mpris.MediaPlayer2.Player.Previous"),
    desc='Audio previous'),

    # Volume control
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 1")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 1")),
    # App launch keybinds
    Key([mod], "F2", lazy.spawn(os.path.expanduser("~/.config/rofi/powermenu/powermenu.sh")), desc="Open rofi app launcher"),
    Key([mod], "F1", lazy.spawn(os.path.expanduser("~/.config/rofi/launchers/text/launcher.sh")), desc="Open rofi app launcher"),
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod, "control"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
           [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0, margin=[15, 15, 8, 8]),
    layout.Max(),
]

widget_defaults = dict(
    font="Hack",
    fontsize=20,
    padding=3,
)
class colors:
    black = '#1A1B26' #black
    grey =  '#2B2B29'
    red =   '#EC7875' #red
    green = '#61C766' #green
    yellow ='#FDD834' #yellow
    blue =  '#42A5F5' #blue
    magenta ='#BA68C8' #magente
    cyan =  '#4DD0E1' #cyan
    white = '#000000'  #white
    pure_white = 'ffffff' #pure_white

#widgets declarations
groupbox = widget.GroupBox(highlight_method='line', highlight_color=colors.black,)
#Cyan color Arrow
arrow1 = widget.TextBox(text="◢", foreground=colors.cyan, fontsize=125, padding=0)
arrow2 = widget.TextBox(text="◢", foreground=colors.magenta, fontsize=125, padding=0, background=colors.cyan)

pulsevolume= widget.PulseVolume(update_interval=0.001, background=colors.magenta, padding=20)

spotify= Spotify(update_interval=0.001, format= "{icon} {artis} - {track}")

windowname = widget.WindowName()


extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        bottom=bar.Bar(
            background=colors.black,
            margin=10,
            widgets=[
                widget.Spacer(30),
                groupbox,
                widget.Spacer(),
                widget.Clock(fontsize=20),
                widget.Spacer(),
                widget.BatteryIcon(),
                widget.Spacer(10)
            ],
            size=50,
        ),
    ),
    Screen(
        bottom=bar.Bar(
            background = colors.black,
            margin = 10,
            widgets = [
                widget.Spacer(),
                groupbox,
                widget.Battery(),
            ],
            size=50),
        top=bar.Bar(
            background = colors.black,
            margin = 10,
                widgets = [
                widget.Spacer(),
                widget.Clock(),
                widget.Spacer(),
                arrow1,
                widget.TextBox(text="Σ", background=colors.cyan, fontsize=30, padding=10),
                widget.CPU(background=colors.cyan, format = '{freq_current}GHz {load_percent}%'),
                widget.Spacer(5),

            ],
            size=50),

        )
    ]


#Autostart apps
@hook.subscribe.startup_once
def autostart():
    lazy.to_screen(0)
    lazy.spawn("alacritty =e tty-clock -C 6 -c")
    lazy.to_screen(1)
    lazy.spawn("google-chrome-stable")
    lazy.to_screen(2)
    lazy.spawn("code")
    lazy.to_screen(0)
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
