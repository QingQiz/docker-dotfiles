#!/usr/bin/env python

import os


# environment
workdir = os.path.abspath(__file__)
workdir = os.path.dirname(workdir)
homedir = os.path.dirname(workdir)

plugins = [
    "tomasr/molokai",
    "tpope/vim-surround",
    "majutsushi/tagbar",
    "preservim/nerdtree",
    "vim-airline/vim-airline",
    "vim-airline/vim-airline-themes",
    "mhinz/vim-startify",
    "Yggdroot/indentLine",
    "jiangmiao/auto-pairs",
    "kshenoy/vim-signature",
    "luochen1990/rainbow",
    "mbbill/undotree",
    "easymotion/vim-easymotion",
    "junegunn/vim-easy-align",
    "lilydjwg/fcitx.vim",
    "tenfyzhong/CompleteParameter.vim",
    "jeaye/color_coded",
    "Valloric/YouCompleteMe",
    "itchyny/vim-haskell-indent",
]

# install vim
os.makedirs(f'{workdir}/.vim/vimfiles', exist_ok=True)
os.makedirs(f'{homedir}/.cache/vim/undo', exist_ok=True)
os.system('pacman -S --noconfirm vim')

# download plugins
os.chdir(f'{workdir}/.vim/vimfiles')
for plugin in plugins:
    os.system(f'git clone https://github.com/{plugin}.git')
os.system('pacman -S --noconfirm vim-ultisnips')

# build jeaye/color_coded
os.chdir(f'{workdir}/.vim/vimfiles')
os.makedirs('color_coded/build', exist_ok=True)
os.chdir('color_coded/build')

os.system('pacman -S --noconfirm lua52 lua')
os.symlink('/usr/lib/libtinfo.so.6', '/usr/lib/libtinfo.so.5')

os.system('cmake ..')
os.system('make -j && make install')
os.system('make clean')

os.remove (f'{workdir}/.vim/vimfiles/color_coded/after/syntax/color_coded.vim')
os.symlink(f'{workdir}/.vim/syntax/color_coded.vim',
           f'{workdir}/.vim/vimfiles/color_coded/after/syntax/color_coded.vim')
os.symlink(f'{workdir}/.config/color_coded',
           f'{homedir}/.config/color_coded')

# build Valloric/YouCompleteMe
os.chdir(f'{workdir}/.vim/vimfiles/YouCompleteMe')
os.system('git submodule update --init --recursive')
os.system('./install.py --clang-completer')

os.symlink(f'{workdir}/.config/ycmd',
           f'{homedir}/.config/ycmd')

# link config files
os.symlink(f'{workdir}/.vim',
           f'{homedir}/.vim')
os.symlink(f'{workdir}/.vimrc',
           f'{homedir}/.vimrc')
