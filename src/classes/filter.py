"""File containing sereval filters."""

# Import for making class into an enumeration
from enum import Enum

# Import matrix class
from classes.matrix import Matrix

class Filter(Enum):
    """
    Sereval filter used for edge detection as Matrix objects.

    Notes
    -----
    Only the horicontal filters are saved. To get the vertical filters,
    the matrices need to be inversed by calling the 'inverse()' method
    of the Matrix class.
    """

    SOEBEL: Matrix = Matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    PREWITT: Matrix = Matrix([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
