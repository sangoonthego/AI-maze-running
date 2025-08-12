import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from src.game.game_engine import GameEngine
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS

def main():
    try:
        game = GameEngine(WINDOW_WIDTH, WINDOW_HEIGHT, FPS)
        game.run()
        
    except KeyboardInterrupt:
        print("\nGame interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 