import pygame
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional

from config.settings import *
from maze.maze_generator import MazeGenerator
from player.player import Player
from ai.ai_controller import AIController
from game.renderer import Renderer
from game.input_handler import InputHandler
from ui.hud import HUD

class GameEngine:
    def __init__(self, width: int, height: int, fps: int):
        pygame.init()
        
        self.width = width
        self.height = height
        self.fps = fps
        
        # Initialize display
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Maze Runner AI")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        self.game_state = "menu"  # "menu", "playing", "paused", "game_over"
        
        # Initialize components
        self.maze_generator = MazeGenerator(MAZE_WIDTH, MAZE_HEIGHT)
        self.maze = None
        self.player = None
        self.ai_controller = None
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()
        self.hud = HUD()
        
        # Game variables
        self.start_time = 0
        self.player_won = False
        self.ai_won = False
        
        # Initialize game
        self.init_game()
    
    def init_game(self):
        # Generate new maze
        self.maze = self.maze_generator.generate_maze()
        
        # Initialize player at start position
        start_pos = self.maze.get_start_position()
        self.player = Player(start_pos[0], start_pos[1], PLAYER_SPEED)
        
        # Initialize AI controller
        self.ai_controller = AIController(self.maze, AI_ALGORITHM)
        
        # Reset game state
        self.start_time = pygame.time.get_ticks()
        self.player_won = False
        self.ai_won = False
        self.game_state = "playing"
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_state == "playing":
                        self.game_state = "paused"
                    elif self.game_state == "paused":
                        self.game_state = "playing"
                
                elif event.key == pygame.K_r:
                    self.init_game()
                
                elif event.key == pygame.K_q:
                    self.running = False
        
        # Handle input for player movement
        if self.game_state == "playing":
            self.input_handler.handle_input(self.player, self.maze)
    
    def update(self):
        if self.game_state != "playing":
            return
        
        # Update player
        if self.player:
            self.player.update()
            
            # Check if player reached goal
            if self.maze.is_goal(self.player.x, self.player.y):
                self.player_won = True
                self.game_state = "game_over"
        
        # Update AI
        if self.ai_controller and not self.ai_won:
            self.ai_controller.update()
            
            # Check if AI reached goal
            ai_pos = self.ai_controller.get_position()
            if self.maze.is_goal(ai_pos[0], ai_pos[1]):
                self.ai_won = True
                self.game_state = "game_over"
    
    def render(self):
        # Clear screen
        self.screen.fill(BLACK)
        
        if self.game_state == "playing":
            # Render maze
            self.renderer.render_maze(self.maze)
            
            # Render player
            if self.player:
                self.renderer.render_player(self.player)
            
            # Render AI
            if self.ai_controller:
                self.renderer.render_ai(self.ai_controller)
            
            # Render HUD
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.hud.render(self.screen, elapsed_time, self.player_won, self.ai_won)
        
        elif self.game_state == "paused":
            self.renderer.render_pause_screen()
        
        elif self.game_state == "game_over":
            self.renderer.render_game_over_screen(self.player_won, self.ai_won)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit() 