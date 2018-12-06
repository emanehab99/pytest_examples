import sys
import os

print(sys.path)
print(os.path.dirname(__file__))
print(os.path.abspath('..'))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(sys.path)

import subfolder
import subfolder.myscript