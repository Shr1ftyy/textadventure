import os 
import sys
import random 
import time

class Room(object):
    """
    This class enables the user to create a room class

    name(string) - name of the room
    connections(list) - a list in the format: [["direction","room_name",True/False for lock]]
    desc(string) - description displayed when entering the room
    items(list) - items you can pick up in the room
    interactives(list) - interactive objects in the room

    """
    def __init__(self, name, desc, connections=None, items=None, interactives=None):
        if (isinstance(name, str)):
            self.name = name
        else:
            raise TypeError("The datatype of the variable 'name' must be of type str\nFound: {type(name)}")

        if (isinstance(desc, str)):
            self.desc = desc
        else:
            raise TypeError(f"The datatype of the variable 'desc' must be of type str\nFound: {type(desc)}" )

        self.connections = connections
        self.desc = desc
        self.items = items
        self.interactives = interactives

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes
