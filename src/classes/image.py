"""File containing the Image class."""

# Import for referencing Image class before creation
from __future__ import annotations

# Import for getting rgb values of the image pixels
from PIL import Image as Pixel_Reader

# Import for displaying image
import matplotlib.pyplot as plt

# Import used classes
from classes.pixel import Pixel
from classes.matrix import Matrix

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
    create_pixel_matrix
        Create a matrix including the pixel and the 8 surrounding pixels.
    traverse_vertically
        TBD!!!!

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

    def get_gray_values(self) -> list[list[int]]:
        """
        Return the gray values of the pixels.

        Returns
        -------
        gray_values: list[list[int]]
            Gray values of the pixels.

        """
        gray_values: list[list[int]] = []

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

    @staticmethod
    def create_pixel_matrix(values: list[list[int]], pos: tuple[int, int]) -> Matrix:
        """
        Create a matrix including the pixel and the 8 surrounding pixels.

        Parameters
        ----------
        values: list[list[int]]
            Gray values of all the pixels
        pos: tuple[int, int]
            Position of the pixel in the format of (row, column).

        Returns
        -------
        pixel_matrix: Matrix
            Matrix containing the pixel and the 8 surrounding pixel.

        """
        pixel_matrix: Matrix = Matrix([
            [values[pos[0] - 1][pos[1] - 1], values[pos[0] - 1][pos[1]],
             values[pos[0] - 1][pos[1] + 1]],
            [values[pos[0]][pos[1] - 1], values[pos[0]][pos[1]],
             values[pos[0]][pos[1] + 1]],
            [values[pos[0] + 1][pos[1] - 1], values[pos[0] + 1][pos[1]],
             values[pos[0] + 1][pos[1] + 1]]])

        return pixel_matrix

    def traverse_vertically(self, differential_filter: Matrix) -> list[list[Pixel]]:
        """
        Traverse the image vertically and differentiate all pixels.

        Parameters
        ----------
        differential_filter: Matrix
            Applied filter to differentiate.

        Returns
        -------
        pixels_differentiated: list[list[Pixel]]
            Differentiated pixels after vertical transverse.

        """
        gray_values: list[list[int]] = self.get_gray_values()
        pixels_differentiated: list[list[Pixel]] = []

        # Ignore the first and last pixel in each row and column
        for row_count, row in enumerate(gray_values[1:-1]):
            print(row_count)
            pixels_differentiated.append([])

            for col_count, _ in enumerate(row[1:-1]):
                # Increment row/column by 1 count as the first row/column was skipped
                pixel_matrix: Matrix = Image.create_pixel_matrix(
                    gray_values, (row_count + 1, col_count + 1))

                # Calculate the differentiated pixel value at the current position
                pixel_value_tmp: int = Matrix.matrix_multiplication(
                    differential_filter, pixel_matrix).get_value_at(1, 1)

                # Append the value as a pixel
                pixels_differentiated[row_count].append(Pixel(
                    pixel_value_tmp, pixel_value_tmp, pixel_value_tmp))

        return pixels_differentiated
