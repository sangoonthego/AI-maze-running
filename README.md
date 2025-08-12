# Maze Runner AI

A maze game where players and AI compete to find the exit first.

## Features

- **Random Maze Generation**: Each game features a different maze
- **Smart AI**: Combines BFS, A* and DFS algorithms to find paths
- **Beautiful Interface**: Uses Pygame with visual effects
- **Scoring System**: Tracks time and performance

## Installation

1. Clone repository:
```bash
git clone <repository-url>
cd ai-maze-runner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## How to Play

- **WASD** or **Arrow Keys**: Move the player
- **R**: Restart game
- **ESC**: Exit game

## Project Structure

```
ai-maze-runner/
├── main.py                 # Entry point
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── game_engine.py  # Game loop and main logic
│   │   ├── renderer.py     # Rendering handler
│   │   └── input_handler.py # Input handler
│   ├── maze/
│   │   ├── __init__.py
│   │   ├── maze_generator.py # Maze generation
│   │   └── maze_solver.py   # Maze solving algorithms
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── bfs.py          # Breadth-First Search
│   │   ├── astar.py        # A* Algorithm
│   │   ├── dfs.py          # Depth-First Search
│   │   └── ai_controller.py # AI controller
│   ├── player/
│   │   ├── __init__.py
│   │   └── player.py       # Player logic
│   └── ui/
│       ├── __init__.py
│       ├── menu.py         # Main menu
│       └── hud.py          # Heads-up display
├── assets/
│   ├── fonts/
│   ├── images/
│   └── sounds/
├── config/
│   └── settings.py         # Game configuration
└── tests/
    ├── __init__.py
    ├── test_maze.py
    └── test_ai.py
```

## AI Algorithms

### BFS (Breadth-First Search)
- Finds the shortest path from start to goal
- Efficient for simple mazes

### A* (A-star)
- Combines heuristics to optimize pathfinding
- Avoids traps and obstacles

### DFS (Depth-First Search)
- Explores unknown paths
- Finds alternative routes when stuck

## Contributing
- Contributors:
   + Nguyen Tuan Ngoc
   + Tang Ngoc Hau
   + Phan Tran Chi Bao
   + Bui Duc Manh

All contributions are welcome! Please create an issue or pull request.

## License

MIT License 