"""Main file of the project."""

import sys

# Import for initializing the window of the user interface
from tkinter import Tk

# Import used classes
from classes.matrix import Matrix
from classes.user_interface import UserInterface

# Dictionary for the different filters
DIFFERENTIAL_FILTERS: dict[str, Matrix] = {
    'differential': Matrix([[-0.5, 0.0, 0.5]]),
    'soebel': Matrix([[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]]),
    'prewitt': Matrix([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
    'soebel_2': Matrix([[1.0, 4.0, 7.0, 4.0, 1.0], [2.0, 10.0, 17.0, 10.0, 2.0],
                        [0.0, 0.0, 0.0, 0.0, 0.0], [-2.0, -10.0, -17.0, -10.0, -2.0],
                        [-1.0, -4.0, -7.0, -4.0, -1.0]]),
    'soebel_3': Matrix([[1.0, 4.0, 9.0, 13.0, 9.0, 4.0, 1.0],
                        [3.0, 11.0, 26.0, 34.0, 26.0, 11.0, 3.0],
                        [3.0, 13.0, 30.0, 40.0, 30.0, 13.0, 3.0],
                        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        [-3.0, -13.0, -30.0, -40.0, -30.0, -13.0, -3.0],
                        [-3.0, -11.0, -26.0, -34.0, -26.0, -11.0, -3.0],
                        [-1.0, -4.0, -9.0, -13.0, -9.0, -4.0, -1.0]])
}

def main() -> int:
    """Execute the project."""
    # Initialize the window
    window = Tk()

    # Initialize the user interface and show it
    user_interface = UserInterface(window, "Differential Filters", 550, 600)
    user_interface.show_window(DIFFERENTIAL_FILTERS, "./../images/")

    # Return Exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
