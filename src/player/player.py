from typing import Tuple

from config.settings import PLAYER_SPEED

class Player:
    def __init__(self, x: int, y: int, speed: int = PLAYER_SPEED):
        self.x = x
        self.y = y
        self.speed = speed
        self.target_x = x
        self.target_y = y
        self.moving = False
    
    def move_to(self, x: int, y: int):
        self.target_x = x
        self.target_y = y
        self.moving = True
    
    def update(self):
        if self.moving:
            self.x = self.target_x
            self.y = self.target_y
            self.moving = False
    
    def get_position(self) -> Tuple[int, int]:
        return (self.x, self.y)
    
    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.moving = False
    
    def reset(self, x: int, y: int):
        self.set_position(x, y) 