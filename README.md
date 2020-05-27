# rpi-last.fm-coverart

This has been tested on a RPI3 running raspbian.

## Installation
```bash
apt install python3-pip
apt install python3-tk
pip3 install pylast
pip3 install guizero[images]
```
## Configure
Be sure to [create](https://www.last.fm/api/) and add a last.fm api key and your username in the `config.ini` file.

More settings are available to play with.

## Run
I use the following script to start the application
It allows to be run from a remote shell and disables the mouse cursor
```bash
#!/bin/bash
export DISPLAY=:0.0
killall unclutter
unclutter -idle 0 &
python3 sound.py
```
## Exit
You can exit the fullscreen application by pressing `esc`.
Killing the script also works fine.

## Example
I've attached an 'Optoma pico pk201' projector to the RPI. This projector's size is almost equal to my RPI.
Leaves a nice project on my wall next to my computer.

<img src="https://i.ibb.co/WnZ7Hw5/Screenshot-from-2020-05-27-13-50-27.png" width="200" height="200" alt="PC" />
<img src="https://i.ibb.co/DtKTf7D/IMG-20200527-134202-01.jpg" width="200" height="200" alt="Projection" />