from guizero import App, Text, Picture
import lastfm
import _thread 
import configparser
import time
import sys
import os
from urllib import request

app = None
message = None
pic = None
toggle = 0
current_track = ""
current_cover_art = ""

# the screensaver disrupts the application (on RPI), so we send a disactive command periodically
def screensaver(onoff):
    os.system('xscreensaver-command -' + ('de' if not onoff else '') + 'activate > /dev/null 2>&1')

def disable_screensaver():
    screensaver(False)

# hide content when no relevant information is received
def hide_content():
    message.hide()
    pic.hide()

# show content if possible
# calling show 2 times after eachother causes the application to flicker, so we avoid that
def show_content():
    if not message.visible:
        message.show()
    if not pic.visible:
        pic.show()

# get the new information from lastfm and try to display it
def update_message():
    global message
    global pic
    global current_track

    # get track from lastfm
    disable_screensaver()
    new_track = lastfm.getuser()    

    if new_track is not None:

        show_content()

        # only update if new content
        if str(new_track) != str(current_track):

            current_track = new_track
            print("-------------------------------")            
            print(str(current_track))

            # get the album that matches the track
            album = current_track.get_album();
            album_title = "" if album is None else album.title

            # format the artist, title and album
            message.value = str(current_track.artist) + "\n" + current_track.title + "\n" + str(album_title)

            # handle cover art
            cover_art = lastfm.update_album_art()
            print(cover_art)
            pic.after(0, update_album_art, args=[cover_art])

    else:
        hide_content()

# update the cover art
def update_album_art(cover_art):
    global pic
    global current_cover_art

    if cover_art is not None:

        # only update if new cover art
        if current_cover_art is not cover_art:

            current_cover_art = cover_art
            image_name = '.coverart.png'

            # download image and update content
            request.urlretrieve(current_cover_art, image_name)
            pic.image = image_name   

    else:        
        pic.image = 'black.png'   

# load settings and setup the application
def start():
    global app
    global message
    global pic

    # load config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    if 'settings' in config:

        #load settings
        settings = config['settings']
        width = int(settings['width'])
        height = int(settings['height'])
        font = settings['font']
        font_size = int(settings['font-size'])
        font_color = settings['font-color']
        refresh_time = int(settings['refresh-time']) * 1000

        # create UI elements
        app = App(title="Cover Art", bg="black")
        pic = Picture(app, image='black.png', width=width, height=height)
        message = Text(app, text="Cover Art", size=font_size, font=font, color=font_color)

        # callback function that is called every #refresh_time seconds
        message.repeat(refresh_time, update_message)

        # display all!
        app.set_full_screen()
        app.display()

if __name__ == "__main__":
    start()


