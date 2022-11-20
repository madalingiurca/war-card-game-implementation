from enum import Enum

STARTING_SCREEN_TEXT = "Pick your deck theme!"
ENDING_CONGRATS = "CONGRATULATIONS!"
ENDING_LOSE = "TOO BAD.."
ENDING_MESSAGE_WIN = "You won the game against Cartman!"
ENDING_MESSAGE_LOST = "You lost the game against Cartman.."
GAME_TITLE = "!!  LET IT BE WAR  !!"


class Colors(Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
