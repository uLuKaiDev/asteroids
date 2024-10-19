import pygame
from constants import *


class Score():
    def __init__(self, point):
        self.player_score = 0
        
    def update(self, point):
        self.player_score += point
    


