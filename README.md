# textadventure - A module for building simple text adventure games in python #
This was created for a school project, a bigger project to aid in building a
much smaller project :D

## Features
 - room.py - allows user to create room objects
 - world.py - world instance, supports serialization for rooms inside it :D (using
 pickle for now)

## Getting Started
First of all you will need to, of course, import the necessary modules:
```
from room import Room
from world import World
```

To create a room instance, make use of the 'Room' object:
```
bedroom = Room(name='bedroom', desc='You are in your bedroom', connections=['west','hallway'], items=['flashlight','book'], interactives=['chest'])
```
A room contains the following attributes:
    name(string) - name of the room
    connections(list,dict,etc.) - connections of the room to other rooms, can be any suitable datatype
    desc(string) - description displayed when entering the room
    items(list) - items you can pick up in the room
    interactives(list) - interactive objects in the room


