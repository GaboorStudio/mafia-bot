import telegram
from Poll import Poll
from telegram.ext import CommandHandler
import time
import enum


class Rules(enum.Enum):
    GodFather = 0
    Mafia = 1
    Citizen = 2
    Doctor = 3
    Detective = 4
    Sniper = 5


class Teams(enum.Enum):
    Mafia = 0
    City = 1


class Player:
    '''Attributes:
        active_game: player's active game
        name: player's profile name
        user_name: player's username
        user_id: player's chat id
        user_data: player's telegram data
        is_alive: is player alive or not
        emoji: player's emoji
    '''

    def __init__(self, name, user_name, user_id, user_data, active_game):
        self.active_game = active_game
        self.name = name
        self.user_name = user_name
        self.user_id = user_id
        self.user_data = user_data
        self.is_alive = True
        self.emoji = None

    def send_day_poll(self):
        pass

    def doTheJob(self):
        pass

    def toString(self):
        pass


class Mafia(Player):

    '''Additional attributes:
        team_mates_username: list of team mates usernames
    '''

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = "!"
        self.team_mates_username = []

    def findTeam(self):
        return "Mafia"

    def findRule(self):
        return Rules.Mafia

    def doTheJob(self):
        # Ask for shot
        pass


class GodFather(Mafia):

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = "!!!"

    def findRule(self):
        return Rules.GodFather


class Citizen(Player):

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = ":)"

    def findTeam(self):
        return Teams.City

    def findRule(self):
        return Rules.Citizen


class Doctor(Citizen):

    '''Additional attributes:
        saved_himself: number of times that doctor saved himself
    '''

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = "+"
        self.saved_himself = 0
        self.maximum_himself_save = 2

    def set_maxiumum_himself_save(self, saves_number):
        self.maximum_himself_save = saves_number

    def findRule(self):
        return Rules.Doctor


class Detective(Citizen):

    '''Detective attributes:
        detections: a dictionary that saves previous detections
    '''

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = "*"
        self.detections = {}

    def findRule(self):
        return Rules.Detective

    def doTheJob(self):
        # Send the poll for detection
        pass


class Sniper(Citizen):

    '''Additional attributes:
        shots: number of sniper's shots
    '''

    def __init__(self, name, user_name, user_id, user_data, active_game):
        super().__init__(name, user_name, user_id, user_data, active_game)
        self.emoji = "->"
        self.shots = 1

    def set_shots(self, number):
        self.shots = number

    def doTheJob(self):
        # Send the poll
        pass

    def findRule(self):
        return Rules.Sniper
