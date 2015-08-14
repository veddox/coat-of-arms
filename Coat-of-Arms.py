#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Coat-of-Arms.py
#
# Copyright 2015 Christopher Borchert <chrisbor@outlook.com>
#
# Licensed under the terms of the MIT license.
#
# I know this is not quite the most efficient code you've ever seen.
# Whatever, it works.
#

from Menu import Menu
from Menu import GuidedMenu

#Menus *m
global startm
global newgamem
global quitm

#Guided menus *gm
global startgamegm
global joingamegm
global loadgamegm
global createplayergm
global createworldgm

def main():
    create_menus()
    startm.execute()
    return 0

def create_menus():
    #Globals...   -.-
    global startm
    global newgamem
    global quitm

    global startgamegm
    global joingamegm
    global loadgamegm
    global createplayergm
    global createworldgm

    #Actual creation
    startm = Menu([], "\n-- Start menu --")
    newgamem = Menu([], "\nStart game or join game?")
    quitm = Menu([] ,"\nDo you really want to leave? :o")

    startgamegm = GuidedMenu([], "\nPlease give the following data to start a new game:")
    joingamegm = GuidedMenu([], "\nPlease follow the instructions to join an existing game:")
    loadgamegm = GuidedMenu([], "\nPlease help me to load the game:")
    createplayergm = GuidedMenu([], "\nPlease choose your player's attributes:")
    createworldgm = GuidedMenu([], "\nPlease choose these parameters to create a new world:")

    #Adding entries just now, to avoid circular references
    startm.entries = [("New Game", newgamem.execute),("Load Game", loadgamegm.execute),("Quit", quitm.execute)]
    newgamem.entries = [("Start game", startgamegm.execute),("Join game", joingamegm.execute),("Return to start menu", startm.execute)]
    quitm.entries = [("Yes", exit),("No", startm.execute),("Return to start menu", startm.execute)]

    startgamegm.add_entries(["Game name:", "Communication e-mail server:", "E-mail account password:", createworldgm.execute, createplayergm.execute])
    joingamegm.add_entries(["Game name:", "Communication e-mail server:", "E-mail account password:", createplayergm.execute])
    loadgamegm.add_entries(["Absolute file path to the save file:"])
    createplayergm.add_entries(["Name:", "Nation:", "Age (Be careful!):"])#, (sexm = Menu([("Female", return "Female"), ("Male", return "Male")])).execute])
    createworldgm.add_entries(["Name:", "Height:", "Width:"])

if __name__ == '__main__':
    main()




