# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from fractions import Fraction

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal


mod = "mod1"
terminal = "alacritty"
myBrowser = "google-chrome-stable"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod, "shift"], "Return", lazy.spawn(
        terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.run_extension(extension.DmenuRun(
        dmenu_promt="~> ",
        fontsize=13,
        dmenu_lines=0,
        dmenu_bottom=True,
        font="JetBrainsMono Nerd Font",
        background="0c2245",
        foreground="ffffff",
    ))),
    # ADD F KEY USES
    Key([], "F6", lazy.spawn("playerctl --player=spotify previous")),
    Key([], "F7", lazy.spawn("playerctl --player=spotify play-pause")),
    Key([], "F8", lazy.spawn("playerctl --player=spotify next")),
    Key([], "F9", lazy.spawn("playerctl --player=spotify play-pause")),
    Key([], "F10", lazy.spawn("playerctl --player=spotify volume 0.1-")),
    Key([], "F11", lazy.spawn("playerctl --player=spotify volume 0.1+")),
]


noborita = {
    "blue": "3451d1",
    "light_blue": "267594",
    "dark_blue": "161f45",
    "white": "ffffff",
    "black": "000000",
    "gray": "26272e",
    "light_gray": "4b4c57",
}


def get_groups():
    spaces = [
        "  ",
        "  ",
        "  ",
        "  ",
        "  ",
        " ﭮ ",
        "  "
    ]
    return [Group(space) for space in spaces]


if __name__ in ["config", "__main__"]:
    groups = get_groups()

for i, group in enumerate(groups, 1):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i),
                lazy.group[group.name].toscreen(),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(group.name, switch_group=False),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus="#b3d4f5",
        border_normal="#002f5e",
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=3,
        margin=8,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    background=noborita["light_gray"],
                    length=10,
                ),
                widget.TextBox(
                    text="   ",
                    foreground=noborita["white"],
                    background=noborita["light_gray"],
                    fontsize=28,
                    padding=0
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["light_gray"],
                    background=noborita["gray"],
                    fontsize=28,
                    padding=0
                ),
                widget.Spacer(
                    background=noborita["gray"],
                    length=20,
                ),
                widget.GroupBox(
                    background=noborita["gray"],
                    highlight_method="block",
                    highlight_color=noborita["light_gray"],
                    this_current_screen_border=noborita["light_gray"],
                    this_screen_border=noborita["light_gray"],
                    other_current_screen_border=noborita["light_gray"],
                    other_screen_border=noborita["light_gray"],
                    foreground=noborita["white"],
                    inactive=noborita["white"],
                    fontsize=20,
                    spacing=4,
                    padding=8,
                    rounded=False,
                    center_aligned=True,
                ),
                widget.TextBox(
                    text=" ",
                    foreground=noborita["gray"],
                    fontsize=28,
                    padding=0
                ),
                widget.Spacer(
                    length=bar.STRETCH
                ),
                widget.TextBox(
                    text=" ",
                    foreground=noborita["blue"],
                    fontsize=28,
                    padding=0
                ),
                widget.TextBox(
                    text="  ",
                    background=noborita["blue"],
                    foreground=noborita["white"],
                    fontsize=28,
                    padding=0
                ),
                widget.CurrentLayout(
                    background=noborita["blue"],
                    fontsize=16,
                    # colour_have_updates="51ddf0"
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["light_blue"],
                    background=noborita["blue"],
                    fontsize=28,
                    padding=0
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["white"],
                    background=noborita["light_blue"],
                    fontsize=28,
                ),
                widget.Memory(
                    background=noborita["light_blue"],
                    fontsize=16,
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["blue"],
                    background=noborita["light_blue"],
                    fontsize=28,
                    padding=0
                ),
                widget.CheckUpdates(
                    no_update_string="Up to Date ",
                    distro="Ubuntu",
                    display_format="{updates} ",
                    background=noborita["blue"],
                    fontsize=16,
                    # colour_have_updates="51ddf0"
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["light_blue"],
                    background=noborita["blue"],
                    fontsize=28,
                    padding=0
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["white"],
                    background=noborita["light_blue"],
                    fontsize=20,
                ),
                widget.Net(
                    format="{down}",
                    background=noborita["light_blue"],
                    border_color=noborita["white"],
                    update_interval=1,
                    fontsize=16,
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["blue"],
                    background=noborita["light_blue"],
                    fontsize=28,
                    padding=0
                ),
                widget.TextBox(
                    text="",
                    foreground=noborita["white"],
                    background=noborita["blue"],
                    fontsize=20,
                ),
                widget.Net(
                    format="{up}",
                    background=noborita["blue"],
                    border_color=noborita["white"],
                    update_interval=1,
                    fontsize=16,
                ),
                widget.TextBox(
                    text="",
                    background=noborita["blue"],
                    foreground=noborita["light_blue"],
                    fontsize=30,
                    padding=0
                ),
                widget.TextBox(
                    text=" ",
                    foreground=noborita["white"],
                    background=noborita["light_blue"],
                    fontsize=20
                ),
                widget.Clock(
                    format="%H:%M",
                    foreground=noborita["white"],
                    background=noborita["light_blue"],
                    fontsize=16
                ),
                widget.Spacer(
                    length=10,
                    background=noborita["light_blue"],
                )
            ],
            32,
            background=noborita["dark_blue"],
            border_width=[0, 0, 1, 0],  # Draw top and bottom borders
            border_color=["ff00ff", "000000", "020c1c",
                          "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
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
