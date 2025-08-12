"""
Tests for Maze Generation
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from maze.maze import Maze
from maze.maze_generator import MazeGenerator

class TestMaze(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.maze = Maze(10, 10)
        self.generator = MazeGenerator(10, 10)
    
    def test_maze_creation(self):
        """Test maze creation"""
        self.assertEqual(self.maze.width, 10)
        self.assertEqual(self.maze.height, 10)
        self.assertEqual(len(self.maze.grid), 10)
        self.assertEqual(len(self.maze.grid[0]), 10)
    
    def test_cell_access(self):
        """Test cell access methods"""
        self.maze.set_cell(5, 5, 2)
        self.assertEqual(self.maze.get_cell(5, 5), 2)
        
        # Test out of bounds
        self.assertEqual(self.maze.get_cell(15, 15), 1)  # Should return wall
    
    def test_start_goal_setting(self):
        """Test start and goal position setting"""
        self.maze.set_start(1, 1)
        self.maze.set_goal(8, 8)
        
        self.assertEqual(self.maze.get_start_position(), (1, 1))
        self.assertEqual(self.maze.get_goal_position(), (8, 8))
        self.assertTrue(self.maze.is_goal(8, 8))
        self.assertFalse(self.maze.is_goal(1, 1))
    
    def test_maze_generation(self):
        """Test maze generation"""
        generated_maze = self.generator.generate_maze()
        
        # Check that maze has start and goal
        self.assertIsNotNone(generated_maze.get_start_position())
        self.assertIsNotNone(generated_maze.get_goal_position())
        
        # Check that start and goal are different
        start = generated_maze.get_start_position()
        goal = generated_maze.get_goal_position()
        self.assertNotEqual(start, goal)
    
    def test_neighbors(self):
        """Test neighbor finding"""
        # Create a simple maze with paths
        for y in range(3):
            for x in range(3):
                self.maze.set_cell(x, y, 0)  # Set as path
        
        neighbors = self.maze.get_neighbors(1, 1)
        expected = [(0, 1), (2, 1), (1, 0), (1, 2)]
        
        for neighbor in expected:
            self.assertIn(neighbor, neighbors)

if __name__ == '__main__':
    unittest.main() 