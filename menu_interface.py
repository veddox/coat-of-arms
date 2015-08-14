#!/usr/bin/python3
#
# A proof-of-concept for a number-menu-based CLI interface.
#
# Copyright (c) 2015 Daniel Vedder
# Licensed under the terms of the MIT license.
#

class Menu:
    def __init__(self, start_entries=[], intro="Please choose an option:"):
        '''
        Create a new menu, optionally initialising it with a list of entries
        (each entry is a tuple of a string and a function name) and an
        intro text to be displayed at the head of the menu.
        '''
        self.entries = start_entries
        self.intro_text = intro

    def add_entry(self, entry, function):
        '''
        Add an entry and the function executed by it to this menu.
        '''
        self.entries.append((str(entry), function))

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
        self.entries[int(choice)-1][1]()


def test():
    m = Menu()
    def f1():
        print("Hello World!")
        m.execute()
    def f2():
        print("Hi there! What's your name?")
        name = input(">>> ")
        print("Nice to meet you, "+name+"!")
        m.execute()
    m.add_entry("Option 1", f1)
    m.add_entry("Option 2", f2)
    m.add_entry("Exit", exit)
    m.execute()

if __name__ == "__main__":
    test()
