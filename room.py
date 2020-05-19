import os 
import sys
import random 
import time

class Room(object):
    """
    This class enables the user to create a room class

    name(string) - name of the room
    connections(list) - a list in the format: [["direction","room_name",True/False for lock]]
    desc(string) - descritption when entering the room
    items(list) - items you can pick up in the room
    interactives(list) - interactive objects in the room

    """
    def __init__(self, name, connections, desc, items, interactives):
        self.name = name
        self.connections = connections
        self.desc = desc
        self.items = items
        self.interactives = interactives
