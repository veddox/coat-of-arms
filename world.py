#!/usr/bin/python3
#
# Coat of arms is an email-based, CLI strategy game of conquest.
# This module holds the representations of all in-game entities.
#
# Copyright (c) 2015 Daniel Vedder, Christopher Borchert
# Licensed under the terms of the MIT license.
#

import xml.etree.ElementTree as xml

global world

class Territory:
    def __init__(self, name, tax, neighbours=[], owner="", units=[]):
        self.name = name
        self.tax = tax
        self.neighbours = neighbours
        self.owner = owner
        self.units = units

    def add_neighbour(self, neighbour):
        "Add a neighbour to this territory (by name)"
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

    def add_unit(self, unit):
        "Add a unit to this territory (by UID)"
        if unit not in self.units:
            self.units.append(unit)

class Unit:
    def __init__(self, uid, max_health, strength, name=""):
        self.uid = uid #A unique id consisting of player name + id number
        self.max_health = self.health = max_health
        self.strength = strength
        self.name = name

    def change_health(self, amount):
        ''' Change the health of this unit by amount. Method returns -1 if the
        unit dies, otherwise returns 0.
        '''
        self.health = self.health + amount
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health <= 0:
            return -1 #replace this with a custom error?
        else: return 0

class Player:
    def __init__(self, name, gold= 0, units=[], territories=[]):
        #TODO replace args with kwargs
        self.name = name
        self.units = units
        self.territories = territories
        self.gold = gold


class World:
    def __init__(self, world_file=None):
        if world_file: parse_world_file(world_file)
        else:
            self.players = self.territories = []

    def parse_world_file(self, file_name):
        "Parse the given world file"
        pass
            
    
