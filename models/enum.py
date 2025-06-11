from enum import Enum

class Action(str, Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    SELECT = 'select'
    HOME = 'home'
    PREVIOUS = 'previous'
    PLAY_PAUSE = 'play/pause'
    SLEEP = 'sleep'
    EXIT = 'exit'