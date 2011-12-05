#!/usr/bin/env python
"""
    Ngoma is an MPlayer clone written in Python as a learning exercise.
    Copyright Okal Otieno, 2011 and beyond.
"""
from mutagen.easyid3 import EasyID3
from sys import argv
from string import capitalize

def print_song_info(song_file):
    song = EasyID3(song_file)
    for k in song.keys():
        print "%s: %s" % (capitalize(k), ', '.join(song[k]))


if __name__ == "__main__":
    song_file = argv[1]
    print_song_info(song_file)
