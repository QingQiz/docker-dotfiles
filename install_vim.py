#!/usr/bin/env python

import os


# environment
workdir = os.path.abspath(__file__)
workdir = os.path.dirname(workdir)
homedir = os.path.dirname(workdir)

# install vim
os.makedirs(f'{workdir}/.vim/vimfiles', exist_ok=True)
os.makedirs(f'{homedir}/.cache/vim/undo', exist_ok=True)
os.system('pacman -S --noconfirm vim')

# download plugins
os.chdir(f'{workdir}/.vim/vimfiles')
os.system('pacman -S --noconfirm vim-ultisnips')

# build jeaye/color_coded
#os.chdir(f'{workdir}/.vim/vimfiles')
#
#os.system('pacman -S --noconfirm lua52 lua')
#os.symlink('/usr/lib/libtinfo.so.6', '/usr/lib/libtinfo.so.5')
#
#os.remove (f'{workdir}/.vim/vimfiles/color_coded/after/syntax/color_coded.vim')
#os.symlink(f'{workdir}/.vim/syntax/color_coded.vim',
#           f'{workdir}/.vim/vimfiles/color_coded/after/syntax/color_coded.vim')
#os.symlink(f'{workdir}/.config/color_coded',
#           f'{homedir}/.config/color_coded')

# build Valloric/YouCompleteMe
#os.chdir(f'{workdir}/.vim/vimfiles/YouCompleteMe')
#
#os.symlink(f'{workdir}/.config/ycmd',
#           f'{homedir}/.config/ycmd')

# link config files
os.symlink(f'{workdir}/.vim', f'{homedir}/.vim')
os.symlink(f'{workdir}/.vimrc', f'{homedir}/.vimrc')

# install junegunn/vim-plug
dst = os.path.join(homedir, '.vim/autoload/plug.vim')
repoUrl = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
os.system(f'curl -fLo {dst} --create-dirs {repoUrl}')
