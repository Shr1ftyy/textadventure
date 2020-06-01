import os 
import sys
import random 
import time

class Room(object):
    """
    This class enables the user to create a room class

    name(string) - name of the room
    connections(list) - a list in the format: [["direction","room_name",True/False for lock]]
        - can be virtually any suitable datatype you want depending on your game's mechanics
    desc(string) - description displayed when entering the room
    items(list) - items you can pick up in the room
    interactives(list) - interactive objects in the room
    inter_items(dict) - dictionary with the interactive objects' names as index and the
                        items inside them in a list.

    """
    def __init__(self, name, desc, connections=None, items=None, interactives=None, inter_items=None):
        if (isinstance(name, str)):
            self.name = name
        else:
            raise TypeError("The datatype of the variable 'name' must be of type str\nFound: {type(name)}")

        if (isinstance(desc, str)):
            self.desc = desc
        else:
            raise TypeError(f"The datatype of the variable 'desc' must be of type str\nFound: {type(desc)}" )

        self.connections = connections
        self.items = items
        self.interactives = interactives
        self.inter_items = inter_items
