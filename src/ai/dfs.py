from typing import List, Tuple, Dict, Optional, Set

from maze.maze import Maze

class DFS:
    def __init__(self, maze: Maze):
        self.maze = maze
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        if start == goal:
            return [start]
        
        visited = set()
        path = []
        
        def dfs_recursive(current_pos: Tuple[int, int], current_path: List[Tuple[int, int]]) -> bool:
            if current_pos == goal:
                path.extend(current_path)
                return True
            
            if current_pos in visited:
                return False
            
            visited.add(current_pos)
            
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    if dfs_recursive(neighbor, current_path + [neighbor]):
                        return True
            
            return False
        
        dfs_recursive(start, [start])
        return path
    
    def explore_area(self, start: Tuple[int, int], max_depth: int = 100) -> Set[Tuple[int, int]]:
        visited = set()
        
        def explore_recursive(pos: Tuple[int, int], depth: int):
            if depth > max_depth or pos in visited:
                return
            
            visited.add(pos)
            
            if depth < max_depth:
                neighbors = self.maze.get_neighbors(*pos)
                for neighbor in neighbors:
                    explore_recursive(neighbor, depth + 1)
        
        explore_recursive(start, 0)
        return visited
    
    def find_alternative_path(self, start: Tuple[int, int], goal: Tuple[int, int], 
                            blocked_positions: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if start == goal:
            return [start]
        
        visited = set()
        path = []
        
        def dfs_avoid_blocks(current_pos: Tuple[int, int], current_path: List[Tuple[int, int]]) -> bool:
            if current_pos == goal:
                path.extend(current_path)
                return True
            
            if current_pos in visited or current_pos in blocked_positions:
                return False
            
            visited.add(current_pos)
            
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in blocked_positions:
                    if dfs_avoid_blocks(neighbor, current_path + [neighbor]):
                        return True
            
            return False
        
        dfs_avoid_blocks(start, [start])
        return path
    
    def find_dead_ends(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        visited = set()
        dead_ends = []
        
        def find_dead_ends_recursive(pos: Tuple[int, int]):
            if pos in visited:
                return
            
            visited.add(pos)
            neighbors = self.maze.get_neighbors(*pos)
            
            # Check if this is a dead end (only one neighbor or no neighbors)
            if len(neighbors) <= 1:
                dead_ends.append(pos)
            
            # Continue exploring
            for neighbor in neighbors:
                if neighbor not in visited:
                    find_dead_ends_recursive(neighbor)
        
        find_dead_ends_recursive(start)
        return dead_ends 