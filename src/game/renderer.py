import pygame
from typing import Tuple

from config.settings import *
from maze.maze import Maze
from player.player import Player
from ai.ai_controller import AIController

class Renderer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font(None, FONT_SIZE)
        
        # Calculate maze offset to center it on screen
        self.maze_offset_x = (WINDOW_WIDTH - MAZE_WIDTH * CELL_SIZE) // 2
        self.maze_offset_y = (WINDOW_HEIGHT - MAZE_HEIGHT * CELL_SIZE) // 2
    
    def render_maze(self, maze: Maze):
        for y in range(maze.height):
            for x in range(maze.width):
                cell = maze.get_cell(x, y)
                screen_x = x * CELL_SIZE + self.maze_offset_x
                screen_y = y * CELL_SIZE + self.maze_offset_y
                
                # Draw cell based on type
                if cell == 1:  # Wall
                    pygame.draw.rect(self.screen, GRAY, 
                                   (screen_x, screen_y, CELL_SIZE, CELL_SIZE))
                elif cell == 2:  # Start
                    pygame.draw.rect(self.screen, GREEN, 
                                   (screen_x, screen_y, CELL_SIZE, CELL_SIZE))
                elif cell == 3:  # Goal
                    pygame.draw.rect(self.screen, RED, 
                                   (screen_x, screen_y, CELL_SIZE, CELL_SIZE))
                else:  # Path
                    pygame.draw.rect(self.screen, WHITE, 
                                   (screen_x, screen_y, CELL_SIZE, CELL_SIZE))
                
                # Draw cell border
                pygame.draw.rect(self.screen, BLACK, 
                               (screen_x, screen_y, CELL_SIZE, CELL_SIZE), 1)
    
    def render_player(self, player: Player):
        screen_x = player.x * CELL_SIZE + self.maze_offset_x
        screen_y = player.y * CELL_SIZE + self.maze_offset_y
        
        # Draw player as a blue circle
        center_x = screen_x + CELL_SIZE // 2
        center_y = screen_y + CELL_SIZE // 2
        radius = CELL_SIZE // 3
        
        pygame.draw.circle(self.screen, BLUE, (center_x, center_y), radius)
        
        # Draw player border
        pygame.draw.circle(self.screen, BLACK, (center_x, center_y), radius, 2)
    
    def render_ai(self, ai_controller: AIController):
        ai_pos = ai_controller.get_position()
        screen_x = ai_pos[0] * CELL_SIZE + self.maze_offset_x
        screen_y = ai_pos[1] * CELL_SIZE + self.maze_offset_y
        
        # Draw AI as a purple triangle
        center_x = screen_x + CELL_SIZE // 2
        center_y = screen_y + CELL_SIZE // 2
        size = CELL_SIZE // 3
        
        points = [
            (center_x, center_y - size),
            (center_x - size, center_y + size),
            (center_x + size, center_y + size)
        ]
        
        pygame.draw.polygon(self.screen, PURPLE, points)
        pygame.draw.polygon(self.screen, BLACK, points, 2)
    
    def render_pause_screen(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Pause text
        text = self.font.render("PAUSED", True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        # Instructions
        instructions = self.font.render("Press ESC to resume, R to restart, Q to quit", True, WHITE)
        instructions_rect = instructions.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(instructions, instructions_rect)
    
    def render_game_over_screen(self, player_won: bool, ai_won: bool):
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        if player_won:
            text = self.font.render("YOU WIN!", True, GREEN)
        elif ai_won:
            text = self.font.render("AI WINS!", True, RED)
        else:
            text = self.font.render("GAME OVER", True, WHITE)
        
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        # Instructions
        instructions = self.font.render("Press R to restart, Q to quit", True, WHITE)
        instructions_rect = instructions.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        self.screen.blit(instructions, instructions_rect)
    
    def render_path(self, path: list, color: Tuple[int, int, int]):
        for x, y in path:
            screen_x = x * CELL_SIZE + self.maze_offset_x
            screen_y = y * CELL_SIZE + self.maze_offset_y
            
            # Draw path as a small circle
            center_x = screen_x + CELL_SIZE // 2
            center_y = screen_y + CELL_SIZE // 2
            radius = CELL_SIZE // 6
            
            pygame.draw.circle(self.screen, color, (center_x, center_y), radius) 