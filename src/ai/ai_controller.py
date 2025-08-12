import random
from typing import List, Tuple, Optional

from config.settings import AI_UPDATE_RATE, AI_SPEED
from maze.maze import Maze
from ai.bfs import BFS
from ai.astar import AStar
from ai.dfs import DFS

class AIController:
    def __init__(self, maze: Maze, algorithm: str = "astar"):
        self.maze = maze
        self.algorithm = algorithm
        
        # Initialize algorithms
        self.bfs = BFS(maze)
        self.astar = AStar(maze)
        self.dfs = DFS(maze)
        
        # AI state
        self.current_pos = maze.get_start_position()
        self.goal_pos = maze.get_goal_position()
        self.path = []
        self.path_index = 0
        self.update_counter = 0
        
        # AI behavior
        self.stuck_counter = 0
        self.last_pos = self.current_pos
        self.explored_areas = set()
        
        # Calculate initial path
        self._calculate_path()
    
    def update(self):
        self.update_counter += 1
        
        # Only update AI every N frames
        if self.update_counter % AI_UPDATE_RATE != 0:
            return
        
        # Check if stuck
        if self.current_pos == self.last_pos:
            self.stuck_counter += 1
        else:
            self.stuck_counter = 0
            self.last_pos = self.current_pos
        
        # If stuck for too long, recalculate path
        if self.stuck_counter > 10:
            self._handle_stuck_situation()
        
        # Move along path
        self._move_along_path()
        
        # Update explored areas
        self.explored_areas.add(self.current_pos)
    
    def _calculate_path(self):
        if self.algorithm == "bfs":
            self.path = self.bfs.find_path(self.current_pos, self.goal_pos)
        elif self.algorithm == "astar":
            self.path = self.astar.find_path(self.current_pos, self.goal_pos)
        elif self.algorithm == "dfs":
            self.path = self.dfs.find_path(self.current_pos, self.goal_pos)
        else:
            # Default to A*
            self.path = self.astar.find_path(self.current_pos, self.goal_pos)
        
        self.path_index = 0
    
    def _handle_stuck_situation(self):
        # Try different strategies
        strategies = [
            self._try_alternative_path,
            self._try_exploration,
            self._try_random_movement
        ]
        
        for strategy in strategies:
            if strategy():
                break
    
    def _try_alternative_path(self) -> bool:
        # Use DFS to find alternative path
        alternative_path = self.dfs.find_alternative_path(
            self.current_pos, self.goal_pos, set()
        )
        
        if alternative_path and len(alternative_path) > 1:
            self.path = alternative_path
            self.path_index = 0
            return True
        
        return False
    
    def _try_exploration(self) -> bool:
        # Find unexplored neighbors
        neighbors = self.maze.get_neighbors(*self.current_pos)
        unexplored = [n for n in neighbors if n not in self.explored_areas]
        
        if unexplored:
            # Move to unexplored neighbor
            next_pos = random.choice(unexplored)
            self.path = [self.current_pos, next_pos]
            self.path_index = 0
            return True
        
        return False
    
    def _try_random_movement(self) -> bool:
        neighbors = self.maze.get_neighbors(*self.current_pos)
        
        if neighbors:
            next_pos = random.choice(neighbors)
            self.path = [self.current_pos, next_pos]
            self.path_index = 0
            return True
        
        return False
    
    def _move_along_path(self):
        if self.path_index < len(self.path):
            next_pos = self.path[self.path_index]
            
            # Check if next position is still valid
            if self._is_valid_move(next_pos):
                self.current_pos = next_pos
                self.path_index += 1
            else:
                # Path is no longer valid, recalculate
                self._calculate_path()
    
    def _is_valid_move(self, pos: Tuple[int, int]) -> bool:
        return (0 <= pos[0] < self.maze.width and 
                0 <= pos[1] < self.maze.height and 
                not self.maze.is_wall(*pos))
    
    def get_position(self) -> Tuple[int, int]:
        return self.current_pos
    
    def get_path(self) -> List[Tuple[int, int]]:
        return self.path[self.path_index:]
    
    def switch_algorithm(self, algorithm: str):
        self.algorithm = algorithm
        self._calculate_path()
    
    def set_goal(self, goal: Tuple[int, int]):
        self.goal_pos = goal
        self._calculate_path()
    
    def reset(self, start_pos: Tuple[int, int]):
        self.current_pos = start_pos
        self.path_index = 0
        self.stuck_counter = 0
        self.explored_areas.clear()
        self._calculate_path() 