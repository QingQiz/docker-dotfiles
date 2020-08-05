FROM archlinux:latest

ARG user=angel
ARG home=/home/$user

ENV HTTP_PROXY "http://10.61.111.75:2340"
ENV HTTPS_PROXY "http://10.61.111.75:2340"

SHELL ["/bin/bash", "-c"]

RUN echo 'Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist && \
    echo -e "[archlinuxcn]\nSigLevel = Never\nServer = https://mirrors.aliyun.com/archlinuxcn/\$arch" >> /etc/pacman.conf && \
    pacman -Syy && \
    pacman -Syu --noconfirm && \
    pacman -S --noconfirm sudo git make cmake gcc clang python3 && \
    useradd -ms /bin/bash $user && \
    mkdir -p $home/.config && \
    mkdir -p $home/.local/share && \
    echo "$user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers


COPY dotfiles $home/.dotfiles
WORKDIR $home/.dotfiles

COPY install_vim.py install_zsh.py ./
RUN ./install_vim.py && ./install_zsh.py

COPY install_i3.py ./
RUN ./install_i3.py

RUN chown $user:$user -R $home

USER angel
WORKDIR $home

RUN git clone https://github.com/powerline/fonts.git && \
    cd fonts && \
    ./install.sh && \
    fc-cache -frv && \
    cd .. && \
    rm -rf fonts

#CMD x11vnc -forever -create -usepw
CMD /bin/zsh

