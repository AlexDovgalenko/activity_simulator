#!/bin/bash
echo "Starting Activity Simulation Script..."
echo "Press `SHIFT+ESC` key to stop the script when finished"

# Change to the directory where your script is located
cd "<Path to project folder>"

# Activate virtual environment
source venv/bin/activate

# run the script
uv run src/simulator.py

# Deactivate virtual environment
deactivate