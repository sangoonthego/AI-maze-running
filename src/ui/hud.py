"""
HUD (Heads-up Display) - Game information overlay
"""
import pygame
from typing import Tuple

from config.settings import *

class HUD:
    def __init__(self):
        """Initialize HUD"""
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.small_font = pygame.font.Font(None, FONT_SIZE - 8)
    
    def render(self, screen: pygame.Surface, elapsed_time: float, 
               player_won: bool, ai_won: bool):
        """Render HUD elements"""
        # Render time
        self._render_time(screen, elapsed_time)
        
        # Render controls
        self._render_controls(screen)
        
        # Render game status
        self._render_status(screen, player_won, ai_won)
    
    def _render_time(self, screen: pygame.Surface, elapsed_time: float):
        """Render elapsed time"""
        time_text = f"Time: {elapsed_time:.1f}s"
        time_surface = self.font.render(time_text, True, WHITE)
        screen.blit(time_surface, (UI_PADDING, UI_PADDING))
    
    def _render_controls(self, screen: pygame.Surface):
        """Render control instructions"""
        controls = [
            "WASD or Arrow Keys: Move",
            "R: Restart",
            "ESC: Pause/Resume",
            "Q: Quit"
        ]
        
        y_offset = WINDOW_HEIGHT - len(controls) * (FONT_SIZE - 4) - UI_PADDING
        
        for i, control in enumerate(controls):
            control_surface = self.small_font.render(control, True, GRAY)
            screen.blit(control_surface, (UI_PADDING, y_offset + i * (FONT_SIZE - 4)))
    
    def _render_status(self, screen: pygame.Surface, player_won: bool, ai_won: bool):
        """Render game status"""
        if player_won:
            status_text = "YOU WIN!"
            color = GREEN
        elif ai_won:
            status_text = "AI WINS!"
            color = RED
        else:
            status_text = "Racing to the goal..."
            color = YELLOW
        
        status_surface = self.font.render(status_text, True, color)
        status_rect = status_surface.get_rect()
        status_rect.centerx = WINDOW_WIDTH // 2
        status_rect.y = UI_PADDING
        screen.blit(status_surface, status_rect)
    
    def render_algorithm_info(self, screen: pygame.Surface, algorithm: str):
        """Render current AI algorithm"""
        algo_text = f"AI Algorithm: {algorithm.upper()}"
        algo_surface = self.small_font.render(algo_text, True, PURPLE)
        screen.blit(algo_surface, (WINDOW_WIDTH - algo_surface.get_width() - UI_PADDING, UI_PADDING)) 