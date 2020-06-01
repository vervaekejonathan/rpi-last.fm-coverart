#!/usr/bin/env python3

import pylast
import configparser


def connect():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'last.fm' in config:
        API_KEY = config['last.fm']['API_KEY']
        API_SECRET = config['last.fm']['API_SECRET']
        username = config['last.fm']['username']
        network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                       username=username)
        user = network.get_user(username)
        return network, user


def getuser():
    try:
        network, user = connect()
        return user.get_now_playing()
    except Exception as e:
        print(e)
        return None


def update_album_art():
    try:
        network, user = connect()
        track = user.get_now_playing()
        artist = track.artist
        album = track.album
        image = track.image[len(track.image)-1]

        if image == "https://lastfm.freetls.fastly.net/i/u/300x300/2a96cbd8b46e442fc41c2b86b821562f.png":
            print("no cover available")
            image = None
        return image
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    getuser()
