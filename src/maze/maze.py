from typing import List, Tuple, Optional
import random

class Maze:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]  # 1 = wall
        self.start_pos = None
        self.goal_pos = None
    
    def get_cell(self, x: int, y: int) -> int:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return 1  # Return wall for out of bounds
    
    def set_cell(self, x: int, y: int, value: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value
    
    def set_start(self, x: int, y: int):
        self.start_pos = (x, y)
        self.set_cell(x, y, 2)  # 2 = start
    
    def set_goal(self, x: int, y: int):
        self.goal_pos = (x, y)
        self.set_cell(x, y, 3)  # 3 = goal
    
    def get_start_position(self) -> Tuple[int, int]:
        return self.start_pos
    
    def get_goal_position(self) -> Tuple[int, int]:
        return self.goal_pos
    
    def is_goal(self, x: int, y: int) -> bool:
        return (x, y) == self.goal_pos
    
    def is_wall(self, x: int, y: int) -> bool:
        return self.get_cell(x, y) == 1
    
    def is_path(self, x: int, y: int) -> bool:
        cell = self.get_cell(x, y)
        return cell == 0 or cell == 2 or cell == 3
    
    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = []
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.width and 
                0 <= new_y < self.height and 
                self.is_path(new_x, new_y)):
                neighbors.append((new_x, new_y))
        
        return neighbors
    
    def get_all_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = []
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                neighbors.append((new_x, new_y))
        
        return neighbors
    
    def print_maze(self):
        symbols = {0: ' ', 1: '#', 2: 'S', 3: 'G'}
        for row in self.grid:
            print(''.join(symbols[cell] for cell in row))
    
    def clear_paths(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != 1:  # Not a wall
                    self.grid[y][x] = 0  # Set to path 