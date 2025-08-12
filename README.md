# Maze Runner AI

Một game mê cung nơi người chơi và AI cùng thi đấu để tìm lối ra trước.

## Tính năng

- **Mê cung ngẫu nhiên**: Mỗi lần chơi là một mê cung khác nhau
- **AI thông minh**: Kết hợp BFS, A* và DFS để tìm đường
- **Giao diện đẹp**: Sử dụng Pygame với hiệu ứng visual
- **Hệ thống điểm**: Theo dõi thời gian và hiệu suất

## Cài đặt

1. Clone repository:
```bash
git clone <repository-url>
cd ai-maze-runner
```

2. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

3. Chạy game:
```bash
python main.py
```

## Cách chơi

- **WASD** hoặc **Arrow Keys**: Di chuyển người chơi
- **R**: Restart game
- **ESC**: Thoát game

## Cấu trúc dự án

```
ai-maze-runner/
├── main.py                 # Entry point
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── game_engine.py  # Game loop và logic chính
│   │   ├── renderer.py     # Xử lý render
│   │   └── input_handler.py # Xử lý input
│   ├── maze/
│   │   ├── __init__.py
│   │   ├── maze_generator.py # Tạo mê cung
│   │   └── maze_solver.py   # Thuật toán giải mê cung
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── bfs.py          # Breadth-First Search
│   │   ├── astar.py        # A* Algorithm
│   │   ├── dfs.py          # Depth-First Search
│   │   └── ai_controller.py # Điều khiển AI
│   ├── player/
│   │   ├── __init__.py
│   │   └── player.py       # Logic người chơi
│   └── ui/
│       ├── __init__.py
│       ├── menu.py         # Menu chính
│       └── hud.py          # Heads-up display
├── assets/
│   ├── fonts/
│   ├── images/
│   └── sounds/
├── config/
│   └── settings.py         # Cấu hình game
└── tests/
    ├── __init__.py
    ├── test_maze.py
    └── test_ai.py
```

## Thuật toán AI

### BFS (Breadth-First Search)
- Tìm đường ngắn nhất từ start đến goal
- Hiệu quả cho mê cung đơn giản

### A* (A-star)
- Kết hợp heuristic để tối ưu hóa tìm đường
- Tránh các bẫy và chướng ngại vật

### DFS (Depth-First Search)
- Khám phá các lối đi chưa biết
- Tìm đường thay thế khi bị kẹt

## Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng tạo issue hoặc pull request.

## License

MIT License 