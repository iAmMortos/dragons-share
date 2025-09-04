import sys
import os

# Get the parent directory of the current script
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add it to the Python path
sys.path.insert(0, parent_dir)
os.chdir(parent_dir)

