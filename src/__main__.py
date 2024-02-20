"""Main file of the project."""

import sys
import time

# Import used classes
from classes.pixel import Pixel
from classes.image import Image

# Path to the image
PATH_TO_IMAGE: str = "../images/Auto.jpg"

def main() -> int:
    image_normal: Image = Image.read_image(PATH_TO_IMAGE)
        
    # Return Exitcode 0 indicating success
    return 0


if __name__ == "__main__":
    sys.exit(main())
