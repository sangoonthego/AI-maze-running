from typing import List, Tuple, Dict, Optional
from collections import deque

from maze.maze import Maze

class BFS:
    def __init__(self, maze: Maze):
        self.maze = maze
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        if start == goal:
            return [start]
        
        # Initialize BFS
        queue = deque([(start, [start])])  # (position, path)
        visited = {start}
        
        while queue:
            current_pos, path = queue.popleft()
            
            # Get neighbors
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor == goal:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        # No path found
        return []
    
    def find_all_paths(self, start: Tuple[int, int]) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
        queue = deque([(start, [start])])
        visited = {start}
        paths = {start: [start]}
        
        while queue:
            current_pos, path = queue.popleft()
            
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    paths[neighbor] = new_path
                    queue.append((neighbor, new_path))
        
        return paths 