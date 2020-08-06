FROM archlinux:latest

ARG user=angel
ARG home=/home/$user

# ENV HTTP_PROXY "http://10.61.111.75:2340"
# ENV HTTPS_PROXY "http://10.61.111.75:2340"

COPY zh_CN /usr/share/i18n/locales/
SHELL ["/bin/bash", "-c"]

# RUN echo 'Server = http://mirrors.163.com/archlinux/$repo/os/$arch'     > /etc/pacman.d/mirrorlist && \
    # echo 'Server = http://mirrors.aliyun.com/archlinux/$repo/os/$arch' >> /etc/pacman.d/mirrorlist && \
    # echo -e "[archlinuxcn]\nSigLevel = Never\nServer = https://mirrors.aliyun.com/archlinuxcn/\$arch" >> /etc/pacman.conf && \
RUN echo -e "[archlinuxcn]\nSigLevel = Never\nServer = https://repo.archlinuxcn.org/\$arch" >> /etc/pacman.conf && \
    echo 'zh_CN.UTF-8 UTF-8' >> /etc/locale.gen && locale-gen && \
    ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone && \
    pacman -Syy && \
    pacman -Syu --noconfirm && \
    pacman -S --noconfirm sudo git make cmake gcc clang python3 psmisc iproute2 && \
    useradd -ms /bin/bash $user && \
    mkdir -p $home/.config && mkdir -p $home/.local/share && \
    echo "$user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    cd $home     && git clone https://github.com/QingQiz/dotfiles .dotfiles && \
    cd .dotfiles && git submodule update --init --recursive

WORKDIR $home/.dotfiles

COPY install_vim.py .
RUN ./install_vim.py

COPY install_zsh.py .
RUN ./install_zsh.py

COPY install_i3.py  .
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

CMD /bin/zsh
