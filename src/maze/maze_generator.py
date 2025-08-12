import random
from typing import List, Tuple, Set
from collections import deque

from maze.maze import Maze

class MazeGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def generate_maze(self, algorithm: str = "recursive_backtracking") -> Maze:
        maze = Maze(self.width, self.height)
        
        if algorithm == "recursive_backtracking":
            self._recursive_backtracking(maze)
        elif algorithm == "kruskal":
            self._kruskal_algorithm(maze)
        elif algorithm == "prim":
            self._prim_algorithm(maze)
        else:
            self._recursive_backtracking(maze)
        
        # Set start and goal positions
        self._set_start_and_goal(maze)
        
        return maze
    
    def _recursive_backtracking(self, maze: Maze):
        # Start with all walls
        for y in range(maze.height):
            for x in range(maze.width):
                maze.set_cell(x, y, 1)
        
        # Start from a random cell
        start_x = random.randint(0, maze.width - 1)
        start_y = random.randint(0, maze.height - 1)
        
        # Ensure start position is odd (for proper maze structure)
        if start_x % 2 == 0:
            start_x = max(1, start_x - 1)
        if start_y % 2 == 0:
            start_y = max(1, start_y - 1)
        
        self._carve_path(maze, start_x, start_y)
    
    def _carve_path(self, maze: Maze, x: int, y: int):
        # Mark current cell as path
        maze.set_cell(x, y, 0)
        
        # Define directions: up, right, down, left
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Check if new position is within bounds and is a wall
            if (0 < new_x < maze.width - 1 and 
                0 < new_y < maze.height - 1 and 
                maze.get_cell(new_x, new_y) == 1):
                
                # Carve wall between current and new cell
                wall_x = x + dx // 2
                wall_y = y + dy // 2
                maze.set_cell(wall_x, wall_y, 0)
                
                # Recursively carve from new cell
                self._carve_path(maze, new_x, new_y)
    
    def _kruskal_algorithm(self, maze: Maze):
        # Initialize with all walls
        for y in range(maze.height):
            for x in range(maze.width):
                maze.set_cell(x, y, 1)
        
        # Create edges between cells
        edges = []
        for y in range(1, maze.height - 1, 2):
            for x in range(1, maze.width - 1, 2):
                # Add edges to right and down neighbors
                if x + 2 < maze.width:
                    edges.append(((x, y), (x + 2, y)))
                if y + 2 < maze.height:
                    edges.append(((x, y), (x, y + 2)))
        
        random.shuffle(edges)
        
        # Union-Find data structure
        parent = {}
        rank = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True
        
        # Process edges
        for (x1, y1), (x2, y2) in edges:
            if union((x1, y1), (x2, y2)):
                # Carve path between cells
                wall_x = (x1 + x2) // 2
                wall_y = (y1 + y2) // 2
                maze.set_cell(wall_x, wall_y, 0)
                maze.set_cell(x1, y1, 0)
                maze.set_cell(x2, y2, 0)
    
    def _prim_algorithm(self, maze: Maze):
        # Initialize with all walls
        for y in range(maze.height):
            for x in range(maze.width):
                maze.set_cell(x, y, 1)
        
        # Start from a random cell
        start_x = random.randint(1, maze.width - 2)
        start_y = random.randint(1, maze.height - 2)
        if start_x % 2 == 0:
            start_x = max(1, start_x - 1)
        if start_y % 2 == 0:
            start_y = max(1, start_y - 1)
        
        # Mark start as visited
        visited = {(start_x, start_y)}
        maze.set_cell(start_x, start_y, 0)
        
        # Add walls to frontier
        frontier = set()
        for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
            new_x, new_y = start_x + dx, start_y + dy
            if (0 < new_x < maze.width - 1 and 
                0 < new_y < maze.height - 1):
                frontier.add((new_x, new_y))
        
        # Process frontier
        while frontier:
            wall_x, wall_y = random.choice(list(frontier))
            frontier.remove((wall_x, wall_y))
            
            # Find the two cells this wall separates
            neighbors = []
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_x, new_y = wall_x + dx, wall_y + dy
                if (0 < new_x < maze.width - 1 and 
                    0 < new_y < maze.height - 1):
                    neighbors.append((new_x, new_y))
            
            # Check if exactly one neighbor is visited
            visited_neighbors = [n for n in neighbors if n in visited]
            if len(visited_neighbors) == 1:
                # Carve the wall
                maze.set_cell(wall_x, wall_y, 0)
                
                # Mark unvisited neighbor as visited
                unvisited = [n for n in neighbors if n not in visited][0]
                visited.add(unvisited)
                maze.set_cell(unvisited[0], unvisited[1], 0)
                
                # Add new walls to frontier
                for dx, dy in [(0, -2), (2, 0), (0, 2), (-2, 0)]:
                    new_x, new_y = unvisited[0] + dx, unvisited[1] + dy
                    if (0 < new_x < maze.width - 1 and 
                        0 < new_y < maze.height - 1 and
                        (new_x, new_y) not in visited):
                        frontier.add((new_x, new_y))
    
    def _set_start_and_goal(self, maze: Maze):
        # Find all path cells
        path_cells = []
        for y in range(maze.height):
            for x in range(maze.width):
                if maze.get_cell(x, y) == 0:  # Path cell
                    path_cells.append((x, y))
        
        if len(path_cells) < 2:
            return
        
        # Set start position (top-left area)
        start_candidates = [(x, y) for x, y in path_cells 
                           if x < maze.width // 3 and y < maze.height // 3]
        if start_candidates:
            maze.set_start(*random.choice(start_candidates))
        else:
            maze.set_start(*path_cells[0])
        
        # Set goal position (bottom-right area)
        goal_candidates = [(x, y) for x, y in path_cells 
                          if x > 2 * maze.width // 3 and y > 2 * maze.height // 3]
        if goal_candidates:
            maze.set_goal(*random.choice(goal_candidates))
        else:
            maze.set_goal(*path_cells[-1]) 