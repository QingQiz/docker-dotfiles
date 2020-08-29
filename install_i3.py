#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


# environment
workdir = os.path.abspath(__file__)
workdir = os.path.dirname(workdir)
homedir = os.path.dirname(workdir)


def install(*args):
    cmd = 'pacman -S --noconfirm ' + ' '.join(args)
    os.system(cmd)


def linkHome(*args):
    for i in args:
        os.system(f'ln -sf {workdir}/{i} {homedir}/{i}')


def linkConfig(*args):
    for i in args:
        os.system(f'ln -sf {workdir}/.config/{i} {homedir}/.config/{i}')


pkglist = [
    "xorg-server",
    "xorg-xinit",
    "i3-gaps",
    "xcompmgr",
    "polybar",
    "rofi",
    "termite",
    "feh",
    "thunar",
    "ttf-font-awesome",
    "awesome-terminal-fonts",
    "powerline-fonts",
    "noto-fonts",
    "noto-fonts-cjk",
    "noto-fonts-emoji",
    "numlockx",
    "pulsemixer",
    "ttf-dejavu",
    "nerd-fonts-dejavu-sans-mono",
    "xorg-server-xvfb",
    # "emacs",
    "xorg-xrandr",
    "tigervnc"
]

cfghome = [
    ".asoundrc",
    ".compton",
    ".Xauthority",
    ".Xdefaults",
    ".xinitrc",
    ".Xmodmap",
    ".xprofile",
    ".Xresources",
    ".Xresources.d",
    ".tmux.conf",
    ".colorrc",
    ".conky",
    # ".spacemacs"
]

cfgcfg = [
    "i3",
    "neofetch",
    "polybar",
    "rofi",
    "Thunar",
    "termite"
]

install (*pkglist)
linkHome(*cfghome)
linkConfig(*cfgcfg)

# os.system(f'git clone https://github.com/syl20bnr/spacemacs {homedir}/.emacs.d')

os.system(f'mkdir -p {homedir}/.vnc')

with open(f'{homedir}/.vnc/xstartup', 'w') as f:
    print('#!/bin/sh', file=f)
    print('unset SESSION_MANAGER',file=f)
    print('unset DBUS_SESSION_BUS_ADDRESS',file=f)
    print('export XKL_XMODMAP_DISABLE=1', file=f)
    print('exec i3', file=f)

os.system(f'chmod a+x {homedir}/.vnc/xstartup')

## fix polybar and transparency
with open(f'{homedir}/.config/i3/config', 'a') as f:
    print('exec_always xcompmgr &')
    print('exec_always $HOME/.scr/__launch_polybar')
