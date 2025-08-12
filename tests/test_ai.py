"""
Tests for AI Algorithms
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from maze.maze import Maze
from ai.bfs import BFS
from ai.astar import AStar
from ai.dfs import DFS

class TestAI(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        # Create a simple test maze
        self.maze = Maze(5, 5)
        
        # Create a simple path: start at (0,0), goal at (4,4)
        # Path: (0,0) -> (1,0) -> (1,1) -> (2,1) -> (2,2) -> (3,2) -> (3,3) -> (4,3) -> (4,4)
        path_cells = [
            (0,0), (1,0), (1,1), (2,1), (2,2), (3,2), (3,3), (4,3), (4,4)
        ]
        
        for x, y in path_cells:
            self.maze.set_cell(x, y, 0)  # Set as path
        
        self.maze.set_start(0, 0)
        self.maze.set_goal(4, 4)
        
        # Initialize AI algorithms
        self.bfs = BFS(self.maze)
        self.astar = AStar(self.maze)
        self.dfs = DFS(self.maze)
    
    def test_bfs_pathfinding(self):
        """Test BFS pathfinding"""
        path = self.bfs.find_path((0, 0), (4, 4))
        
        # Should find a path
        self.assertIsNotNone(path)
        self.assertGreater(len(path), 0)
        
        # Start and end should be correct
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (4, 4))
        
        # All positions should be valid
        for x, y in path:
            self.assertTrue(self.maze.is_path(x, y))
    
    def test_astar_pathfinding(self):
        """Test A* pathfinding"""
        path = self.astar.find_path((0, 0), (4, 4))
        
        # Should find a path
        self.assertIsNotNone(path)
        self.assertGreater(len(path), 0)
        
        # Start and end should be correct
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (4, 4))
        
        # All positions should be valid
        for x, y in path:
            self.assertTrue(self.maze.is_path(x, y))
    
    def test_dfs_pathfinding(self):
        """Test DFS pathfinding"""
        path = self.dfs.find_path((0, 0), (4, 4))
        
        # Should find a path
        self.assertIsNotNone(path)
        self.assertGreater(len(path), 0)
        
        # Start and end should be correct
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (4, 4))
        
        # All positions should be valid
        for x, y in path:
            self.assertTrue(self.maze.is_path(x, y))
    
    def test_no_path(self):
        """Test when no path exists"""
        # Create a maze with no path to goal
        isolated_maze = Maze(3, 3)
        isolated_maze.set_cell(0, 0, 0)  # Start
        isolated_maze.set_cell(2, 2, 0)  # Goal
        isolated_maze.set_start(0, 0)
        isolated_maze.set_goal(2, 2)
        
        bfs = BFS(isolated_maze)
        path = bfs.find_path((0, 0), (2, 2))
        
        # Should return empty path
        self.assertEqual(path, [])
    
    def test_same_position(self):
        """Test pathfinding to same position"""
        path = self.bfs.find_path((0, 0), (0, 0))
        self.assertEqual(path, [(0, 0)])

if __name__ == '__main__':
    unittest.main() 