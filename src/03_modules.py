"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print out the command line arguments in sys.argv, one per line:
print("Command line arguments passed in:")
[print(arg) for arg in sys.argv]
print("...end of list.\n")

# Print out the OS platform you're using:
print(f"OS platform: {sys.platform}\n")

# Print out the version of Python you're using:
print(f"Python version: {sys.version}\n")

# Print the current process ID
print(f"Current process ID: {os.getpid()}\n")

# Print the current working directory (cwd):
print(f"Current working directory (cwd): {os.getcwd()}\n")

# Print out your machine's login name
print(f"Laptop's login name: {os.getlogin()}\n")
