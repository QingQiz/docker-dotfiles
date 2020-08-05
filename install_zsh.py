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


# install zsh and change default shell to zsh
install('zsh', 'zsh-syntax-highlighting', 'thefuck')
os.system('sudo -u angel -- chsh -s /bin/zsh')

# install oh-my-zsh
os.chdir(workdir)
os.system('git clone https://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh')
os.makedirs('.zsh/zfunctions')
os.chdir('.zsh')
os.system('git clone https://github.com/zsh-users/zsh-autosuggestions.git')
os.system('git clone https://github.com/sindresorhus/pure.git')

os.symlink(f'{workdir}/.zsh/pure.zsh', 'zfunctions/pure')
os.symlink(f'{workdir}/.zsh/async.zsh', 'zfunctions/async')

# link config files
linkHome('.oh-my-zsh', '.bashrc', '.zsh', '.zshrc', '.colorrc')
