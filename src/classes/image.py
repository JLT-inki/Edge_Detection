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
    traverse
        Traverse the image vertically and differentiate all pixels.

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
            rgb_values: list[tuple[float, float, float]] = img.getdata()
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
        pixel_values: list[list[tuple[float, float, float]]] = []

        for count, row in enumerate(self.get_pixels()):
            pixel_values.append([])

            for pixel in row:
                pixel_values[count].append(pixel.get_rgb_values())

        plt.imshow(pixel_values)
        plt.show()

    @staticmethod
    def create_pixel_matrix(values: list[list[float]], pos: tuple[int, int],
                            size: tuple[int, int]) -> Matrix:
        """
        Create a matrix including the pixel and the 8 surrounding pixels.

        Parameters
        ----------
        values: list[list[float]]
            Gray values of all the pixels
        pos: tuple[int, int]
            Position of the pixel in the format of (row, column).

        Returns
        -------
        pixel_matrix: Matrix
            Matrix containing the pixel and the 8 surrounding pixel.

        """
        # Get the indices for the height and width
        height: int = int(size[0] / 2)
        width: int = int(size[1] / 2)

        pixel_matrix: Matrix = Matrix([
            [values[row][col] for col in range(pos[1] - width, pos[1] + width + 1)]
            for row in range(pos[0] - height, pos[0] + height + 1)])

        return pixel_matrix

    def traverse(self, differential_filter: Matrix) -> list[list[Pixel]]:
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
        # Get the grayscale values of the image
        gray_values: list[list[float]] = self.get_gray_values()

        # Initialize the return value
        pixels_differentiated: list[list[Pixel]] = []

        # Get the number of rows and columns of the differential filter
        rows_filter: int = differential_filter.get_number_of_rows()
        cols_filter: int = differential_filter.get_number_of_columns()

        # Calculate the border to ignore; Tuple[rows, columns]
        border: tuple[int, int] = (
            rows_filter - 2 if rows_filter > 3 else 1,
            cols_filter - 2 if cols_filter > 3 else 1)

        # Ignore the border of the image
        for row_count, row in enumerate(gray_values[border[0]:-border[0]]):
            print(row_count)
            pixels_differentiated.append([])

            for col_count in range(len(row[border[1]:-border[1]])):
                # Get the sub matrix for both directions
                pixel_matrix_x: Matrix = Image.create_pixel_matrix(
                    gray_values, (row_count, col_count), (rows_filter, cols_filter))
                pixel_matrix_y: Matrix = Image.create_pixel_matrix(
                    gray_values, (row_count, col_count), (cols_filter, rows_filter))

                # Calculate the differentiated pixel value at the current position
                gradient_x: float = pixel_matrix_x.apply_filter(
                    differential_filter).get_sum()
                gradient_y: float = pixel_matrix_y.apply_filter(
                    differential_filter.transpose()).get_sum()
                gradient_absolute: int = int(
                    (abs(gradient_x) ** 2 + abs(gradient_y) ** 2) ** 0.5)

                pixels_differentiated[row_count].append(Pixel(
                    gradient_absolute, gradient_absolute, gradient_absolute))

        return pixels_differentiated
