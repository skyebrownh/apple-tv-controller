class MenuAction:
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

    def get_actions(self):
        return [
            value for name, value in vars(self.__class__).items()
            if not name.startswith('__') and not callable(value)
        ]