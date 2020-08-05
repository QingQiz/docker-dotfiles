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
    "compton",
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
    "x11vnc",
    "xorg-server-xvfb"
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
    ".conky"
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
