import os 
import sys
import random 
import time

class World(object):
    """
    This class creates a serializable model of a world for the user

    """

    def __init__(self):
        self.rooms = []

    def addRoom(self, room):
        if not isinstance(room, Room):
          raise TypeError("The added room must be "
                          "an instance of class 'Room'. "
                          "Found: " + type(Room))

        elif room.name is None or not isinstance(room.connections, str):
            raise TypeError("You must define a name"
                            "with type string for the room."
                            "Found: " + type(room.name))

        elif room.connections is None or not isinstance(room.connections, str):
            raise TypeError("You must have connections"
                            "with type list for the room."
                            "Found: " + type(room.connections))

        elif room.desc is None or not isinstance(room.desc, str):
            raise TypeError("You must have a description"
                            "with type string for the room."
                            "Found: " + type(room.desc))

        else:
            self.rooms.append(room)

    def load(self, world):

