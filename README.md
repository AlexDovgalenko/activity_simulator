# Activity Simulator

A simple Python script that simulates mouse movements and scrolling to prevent systems from going idle or locking. Useful for maintaining an "active" status during presentations, downloads, or when working with applications that require constant activity.

## Features

- Simulates random mouse movements and scrolling actions
- Returns cursor to original position after movements
- Configurable timing between actions
- Safety feature with PyAutoGUI's FAILSAFE (preventing mouse from going off-screen)
- Easy termination with customizable key combination (`Shift + Esc` by default)
- Cross-platform compatibility

## Requirements

- Python 3.9 or higher
- Required packages:
    - pyautogui
    - pynput
    - keyboard
    - pyobjc (macOS only)
    - python3-xlib (Linux only)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd activity_simulator
```

2. Create and activate a virtual environment:

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install uv
uv pip install -e .
```

## Usage

You can run the simulator using one of the provided launcher scripts:

- Windows: Run `windows.bat`
- macOS: Run `macos.command`
- Linux: Run `linux.sh`

Or directly using Python:
```bash
python src/simulator.py
```

### Controls
- To stop the simulation, press `Shift + Esc`
- Moving your mouse to any screen corner will trigger PyAutoGUI's failsafe and stop the script

### Configuration
The script includes several configurable parameters in `simulator.py`:
- `MOVEMENT_DURATION`: Duration of mouse movements (default: 0.2 seconds)
- `SLEEP_INTERVAL`: Interval between actions (default: 0.2 seconds)
- `EXIT_KEYS`: Customizable key combination to exit the script

## Development

This project uses:
- `ruff` for code formatting and linting
- `pytest` for testing
- `uv` for dependency management
