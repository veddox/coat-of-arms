#!/usr/bin/python3
#
# Just the menus.
#
# Copyright (c) 2015 Daniel Vedder & Christopher Borchert
# Licensed under the terms of the MIT license.
#

from types import FunctionType

class Menu:
    def __init__(self, start_entries=[], intro="Please choose an option:", back_entry=[True, "startm"]):
        '''
        Create a new menu, optionally initialising it with a list of entries
        (each entry is a tuple of a string and a function name) and an
        intro text to be displayed at the head of the menu.
        '''
        self.entries = start_entries
        self.intro_text = intro
        self.base_menu = back_entry[1]
        self.base_menu_active = back_entry[0]
        '''print(self.base_menu_active)
        if self.base_menu_active:
            if self.entries:
                print("Hello")
                self.entries.append(("> Back to start menu", self.jump_to_base_menu))
            else:
                print("else")
                self.entries = [("> Back to start menu", self.jump_to_base_menu)]

    def jump_to_base_menu(self):
        aim = self.base_menu+".execute"
        exec(aim)

    def set_base_menu(base_menu_active=True, base_menu="startm"):
        self.base_menu = base_menu
        self.base_menu_active = base_menu_active'''


    def add_entry(self, entry, function):
        '''
        Add an entry and the function executed by it to this menu.
        '''
        if self.base_menu_active:
            self.entries = self.entries[:-1].append((entry, function)).append(self.entries[-1])
        else: self.entries.append((str(entry), function))

    def execute(self):
        '''
        Show this menu and execute the function the user chooses.
        '''
        def valid_input(s, number_range):
            "Is this input valid for this range of number?"
            try:
                if not s or int(s)-1 not in number_range: return False
            except ValueError: return False
            return True

        print(self.intro_text)
        for i in range(len(self.entries)):
            print(str(i+1)+") "+self.entries[i][0])
        choice = input(">>> ")
        while not valid_input(choice, range(len(self.entries))):
            print("Invalid input! Please choose again:")
            choice = input(">>> ")
      #  try:
        self.entries[int(choice)-1][1]()
      #  except Exception as e:
            #print("Sorry. An error occured. Please try again.")
            #print(e)
            #self.execute()



#Guides the user through a couple of questions automatically
class GuidedMenu:
    #inits questions, maybe data and the headline of the guided menu
    def __init__(self, start_entries=[], intro="Please type all parameters:"):
        self.entries = start_entries
        self.intro_text = intro

    #adds a new entry and maybe the related data, too
    def add_entry(self, entry, data=None):
        self.entries.append([entry, data])

    #adds a bunch of entries by calling add_entry for every parsed list element
    def add_entries(self, entries=[]):
        for i in range(len(entries)):
            self.add_entry(entries[i])

    #processes the menu: gives questions and takes the answers
    def execute(self):
        print(self.intro_text)
        for i in range(len(self.entries)):
            if isinstance(self.entries[i][0], str):
                print(str(i+1)+".: "+self.entries[i][0])
                self.entries[i][1] = input(">>> ")
            else:
                self.entries[i][0]()
