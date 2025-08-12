import heapq
from typing import List, Tuple, Dict, Optional, Set

from maze.maze import Maze

class AStar:
    def __init__(self, maze: Maze):
        self.maze = maze
    
    def heuristic(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> float:
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
    
    def find_path(self, start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        if start == goal:
            return [start]
        
        # Priority queue: (f_score, position, g_score, path)
        open_set = [(0, start, 0, [start])]
        closed_set = set()
        
        # g_score: cost from start to current position
        g_scores = {start: 0}
        
        while open_set:
            f_score, current_pos, g_score, path = heapq.heappop(open_set)
            
            if current_pos == goal:
                return path
            
            if current_pos in closed_set:
                continue
            
            closed_set.add(current_pos)
            
            # Check neighbors
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue
                
                # Cost to move to neighbor (1 for adjacent cells)
                tentative_g_score = g_score + 1
                
                if (neighbor not in g_scores or 
                    tentative_g_score < g_scores[neighbor]):
                    
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    
                    new_path = path + [neighbor]
                    heapq.heappush(open_set, (f_score, neighbor, tentative_g_score, new_path))
        
        # No path found
        return []
    
    def find_path_with_obstacles(self, start: Tuple[int, int], goal: Tuple[int, int], 
                                obstacles: Set[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """Find path avoiding specific obstacles"""
        if start == goal:
            return [start]
        
        open_set = [(0, start, 0, [start])]
        closed_set = set()
        g_scores = {start: 0}
        
        while open_set:
            f_score, current_pos, g_score, path = heapq.heappop(open_set)
            
            if current_pos == goal:
                return path
            
            if current_pos in closed_set:
                continue
            
            closed_set.add(current_pos)
            
            neighbors = self.maze.get_neighbors(*current_pos)
            
            for neighbor in neighbors:
                if neighbor in closed_set or neighbor in obstacles:
                    continue
                
                tentative_g_score = g_score + 1
                
                if (neighbor not in g_scores or 
                    tentative_g_score < g_scores[neighbor]):
                    
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    
                    new_path = path + [neighbor]
                    heapq.heappush(open_set, (f_score, neighbor, tentative_g_score, new_path))
        
        return [] 