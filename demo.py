import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.maze.maze_generator import MazeGenerator
from src.maze.maze import Maze
from src.ai.bfs import BFS
from src.ai.astar import AStar
from src.ai.dfs import DFS

def demo_maze_generation():
    print("=== Maze Generation Demo ===")
    generator = MazeGenerator(15, 15)
    # gen maze using algos
    algorithms = ["recursive_backtracking", "kruskal", "prim"]
    
    for algorithm in algorithms:
        print(f"\nGenerating maze using {algorithm}...")
        maze = generator.generate_maze(algorithm)
        
        print(f"Start: {maze.get_start_position()}")
        print(f"Goal: {maze.get_goal_position()}")
        
        # Print a small section of the maze
        print("Maze preview (5x5 section):")
        for y in range(min(5, maze.height)):
            row = ""
            for x in range(min(5, maze.width)):
                cell = maze.get_cell(x, y)
                if cell == 0:
                    row += " "
                elif cell == 1:
                    row += "#"
                elif cell == 2:
                    row += "S"
                elif cell == 3:
                    row += "G"
            print(row)

def demo_ai_algorithms():
    print("\n=== AI Pathfinding Demo ===")
    
    # Create a simple test maze
    maze = Maze(10, 10)
    
    # Create a simple path
    path_cells = [
        (0,0), (1,0), (1,1), (2,1), (2,2), (3,2), (3,3), (4,3), (4,4)
    ]
    
    for x, y in path_cells:
        maze.set_cell(x, y, 0)
    
    maze.set_start(0, 0)
    maze.set_goal(4, 4)
    
    # Test different algorithms
    algorithms = [
        ("BFS", BFS(maze)),
        ("A*", AStar(maze)),
        ("DFS", DFS(maze))
    ]
    
    for name, algorithm in algorithms:
        print(f"\nTesting {name}...")
        path = algorithm.find_path((0, 0), (4, 4))
        
        print(f"Path length: {len(path)}")
        print(f"Path: {path}")

def main():
    print("Maze Runner AI - Demo")
    print("=" * 30)
    
    try:
        demo_maze_generation()
        demo_ai_algorithms()
        
        print("\n=== Demo Complete ===")
        print("To run the full game, use: python main.py")
        
    except Exception as e:
        print(f"Error during demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 