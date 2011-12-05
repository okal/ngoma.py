#!/usr/bin/env python
"""
    Ngoma is an MPlayer clone written in Python as a learning exercise.
    Copyright Okal Otieno, 2011 and beyond.
"""
import pygame
import time

from mutagen.easyid3 import EasyID3
from sys import argv, stdout
from string import capitalize


def print_song_info(song_file):
    song = EasyID3(song_file)
    for k in song.keys():
        print "%s: %s" % (capitalize(k), ', '.join(song[k]))

def play_song(song_file):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        stdout.write(".")
    return
    

if __name__ == "__main__":
    song_file = argv[1]
    print_song_info(song_file)
    play_song(song_file)
    
