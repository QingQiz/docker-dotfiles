# docker-dotfiles

![aRB6mj.png](https://s1.ax1x.com/2020/08/07/aRB6mj.png)

## Build

```shell
git clone https://github.com/QingQiz/docker-dotfiles
cd docker-dotfiles
docker build -t sofeeys/archlinux-i3wm .
```

or

```shell
docker pull sofeeys/archlinux-i3wm
```

## Run

server

```shell
docker run -itd --name i3 -p 5900:5900 -v ~:/home/angel/workspace/host:rw sofeeys/archlinux-i3wm
```

client

```shell
vncviewer your-server-address
```

