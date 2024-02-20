"""Main file of the project."""

import sys
import time

# Import used classes
from classes.pixel import Pixel
from classes.image import Image
from classes.matrix import Matrix

# Dictionary for the different filters
DIFFERENTIAL_FILTERS: dict[str, Matrix] = {
    'soebel': Matrix([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
    'prewitt': Matrix([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
}

# Path to the image
PATH_TO_IMAGE: str = "../images/Bild1.jpg"

def main() -> int:
    image_normal: Image = Image.read_image(PATH_TO_IMAGE)
    #image_normal.show_image()
    a = Image(image_normal.traverse_vertically(DIFFERENTIAL_FILTERS['soebel']))
    a.show_image()

        
    # Return Exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
