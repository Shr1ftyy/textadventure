import os 
import sys
import random 
import time
import pickle
import json
import room

class World():
    """
    This class creates a serializable model of a world for the user

    Attributes:
    rooms - list of Room objects defined by the user

    """

    def __init__(self):
        self.rooms = {}

    # __getstate__ function for class serialization - called by pickle module
    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def addRoom(self, r):
        if not isinstance(r, room.Room):
            raise TypeError("The added room must be "
                    "an instance of class 'Room'. "
                    "Found: " + str(type(r)))

        elif r.name is None or not isinstance(r.name, str):
            raise TypeError("You must define a name "
                    "with type string for the room."
                    "Found: " + str(type(r.name)))


        elif r.desc is None or not isinstance(r.desc, str):
            raise TypeError("You must have a description "
                    "with type string for the room."
                    "Found: " + str(type(r.desc)))

        else:
            self.rooms[r.name] = r

    def load(self, world='world.pickle'):
        self.rooms = pickle.load(open(str(world), 'rb'))

    def save(self, dirname='world.pickle'):
        if not isinstance(dirname, str):
            raise TypeError("The datatype of the variable 'dirname' must be of type str\nFound: {type(dirname)}")

        dirname = dirname.strip()

        if len(dirname.split("."))== 1:
            dirname += ".pickle"

        if dirname.split(".")[1] != "pickle":
            raise ValueError("""You must enter the file extenstion for the save file as '.pickle'
                            Found: {''.join(dirname.split('.')[1:]}""")

        if os.path.exists(dirname):
            cont = input(f"The save file {dirname} would you like to overwrite it? (y/n)").lower().strip()
            if cont =='y':
                pickle.dump(self.rooms, open(dirname, 'wb+'))
                print('done')
            else: 
                pass

        pickle.dump(self.rooms, open(dirname, 'wb+'))

        print('done')
