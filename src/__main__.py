"""Main file of the project."""

import sys

# Import used classes
from classes.image import Image
from classes.matrix import Matrix

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

# Path to the images
PATH_TO_IMAGES: dict[int, str] = {
    1: "../images/Car.jpg",
    2: "../images/Church.jpg",
    3: "../images/Circle.jpg",
    4: "../images/Sydney.jpg"
}

def main() -> int:
    """Execute the project."""
    # Read the original image
    image_normal: Image = Image.read_image(PATH_TO_IMAGES[1])

    # Traverse the image and show it
    image_traversed = Image(image_normal.traverse(DIFFERENTIAL_FILTERS['soebel']))
    image_traversed.show_image()

    # Return Exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
