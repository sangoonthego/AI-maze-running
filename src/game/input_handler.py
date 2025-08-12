import pygame
from typing import Tuple

from player.player import Player
from maze.maze import Maze

class InputHandler:
    def __init__(self):
        self.keys_pressed = set()
    
    def handle_input(self, player: Player, maze: Maze):
        keys = pygame.key.get_pressed()
        
        # Get current position
        current_x, current_y = player.x, player.y
        
        # Check for movement keys
        new_x, new_y = current_x, current_y
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            new_y -= 1
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            new_y += 1
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            new_x -= 1
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            new_x += 1
        
        # Check if new position is valid (within bounds and not a wall)
        if self.is_valid_move(new_x, new_y, maze):
            player.move_to(new_x, new_y)
    
    def is_valid_move(self, x: int, y: int, maze: Maze) -> bool:
        # Check bounds
        if x < 0 or x >= maze.width or y < 0 or y >= maze.height:
            return False
        
        # Check if cell is not a wall
        cell = maze.get_cell(x, y)
        return cell != 1  # 1 represents wall 