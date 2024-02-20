"""File containing the Image class."""

# Import for referencing Image class before creation
from __future__ import annotations

# Import for getting rgb values of the image pixels
from PIL import Image as Pixel_Reader

# Import for displaying image
import matplotlib.pyplot as plt

# Import Pixel class
from classes.pixel import Pixel

class Image:
    """
    A class representing one Image.

    Attributes
    ----------
    pixels: list[list[Pixel]]
        Pixels of the image.

    Methods
    -------
    get_pixels
        Return the pixels of the image.
    get_gray_values
        Return the gray values of the pixels.
    read_image
        Read RGB values of an image an create an Image object with the values.
    show_image
        Display an Image object.

    """

    def __init__(self, pixels: list[list[Pixel]]) -> None:
        """
        Initialize one Image object with the given attribute.

        Parameters
        ----------
        pixels: list[list[Pixel]]
            Pixels of the image.

        """        
        self.pixels = pixels

    def get_pixels(self) -> list[list[Pixel]]:
        """
        Return the pixels of the image.

        Returns
        -------
        self.pixels: list[list[pixels]]
            Pixels of the image.

        """
        return self.pixels

    def get_gray_values(self) -> list[list[float]]:
        """
        Return the gray values of the pixels.

        Returns
        -------
        gray_values: list[list[float]]
            Gray values of the pixels.

        """
        gray_values: list[list[float]] = []

        for count, row in enumerate(self.get_pixels()):
            gray_values.append([])

            for pixel in row:
                gray_values[count].append(pixel.get_gray_value())

        return gray_values

    @staticmethod
    def read_image(path_to_image: str) -> Image:
        """
        Read RGB values of an image an create an Image object with the values.

        Parameters
        ----------
        path_to_image: str
            Path to the image of which the Image object is to be generated.

        Returns
        -------
        image_new: Image
            Newly created Image object.

        """
        with Pixel_Reader.open(path_to_image) as img:
            rgb_values: list[tuple[int, int, int]] = img.getdata()
            image_width: int = img.size[0]

        # Initialize the Pixel objects
        pixel_list: list[list[Pixel]] = []
        current_row: int = -1

        for count, pixel in enumerate(rgb_values):
            # Switch to the enxt row if an entire row has been initialized
            if count % image_width == 0:
                pixel_list.append([])
                current_row += 1

            pixel_list[current_row].append(Pixel(
                pixel[0], pixel[1], pixel[2]))

        # Create and return the Image object
        image_new: Image = Image(pixel_list)

        return image_new

    def show_image(self) -> None:
        """Display an Image object."""
        pixel_values: list[list[tuple[int, int, int]]] = []

        for count, row in enumerate(self.get_pixels()):
            pixel_values.append([])

            for pixel in row:
                pixel_values[count].append(pixel.get_rgb_values())

        plt.imshow(pixel_values)
        plt.show()
