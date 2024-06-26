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
    add_image_to_plot
        Add the image to the plot to later display them.
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

        Notes
        -----
        The grayscale values of the pixels are cast to float as they are later
        used as the values of a Matrix object which only accepts floats.

        """
        gray_values: list[list[float]] = []

        for count, row in enumerate(self.get_pixels()):
            gray_values.append([])

            for pixel in row:
                gray_values[count].append(float(pixel.get_gray_value()))

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

    def add_image_to_plot(self, title: str, grayscale: bool = False) -> None:
        """
        Add the image to the plot to later display them.

        Parameters
        ----------
        title: str
            Title of the image to identify it on the display.
        grayscale:
            Boolean indicating whether the image shall be shown in grayscale. The
            default value is False, indicating that the image shall be shown in RGB.

        """
        pixel_values: list[list[tuple[float, float, float]]] = []

        for count, row in enumerate(self.get_pixels()):
            pixel_values.append([])

            for pixel in row:
                if grayscale:
                    pixel_values[count].append(
                        (pixel.get_gray_value(), pixel.get_gray_value(),
                         pixel.get_gray_value()))
                else:
                    pixel_values[count].append(pixel.get_rgb_values())

        plt.imshow(pixel_values)
        plt.axis('off')
        plt.title(title)

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

        # Create a Matrix object with the grayscale values to create sub matrices of it
        gray_values_as_matrix: Matrix = Matrix(gray_values)

        # Initialize the return value
        pixels_differentiated: list[list[Pixel]] = []

        # Get the size of the filter (Number of rows, Number of columns)
        filter_size: tuple[int, int] = (differential_filter.get_number_of_rows(),
                                        differential_filter.get_number_of_columns())

        # Calculate the border to ignore; Tuple[rows, columns]
        border: tuple[int, int] = (
            filter_size[0] - 2 if filter_size[0] > 3 else 1,
            filter_size[1] - 2 if filter_size[1] > 3 else 1)

        # Ignore the border of the image
        for row_count, row in enumerate(gray_values[border[0]:-border[0]]):
            pixels_differentiated.append([])

            for col_count in range(len(row[border[1]:-border[1]])):
                # Get sub matrices for both directions
                sub_matrix_x: Matrix = gray_values_as_matrix.create_sub_matrix(
                    (row_count, col_count), (filter_size[0], filter_size[1]))
                sub_matrix_y: Matrix = gray_values_as_matrix.create_sub_matrix(
                    (row_count, col_count), (filter_size[1], filter_size[0]))

                # Calculate the differentiated pixel value at the current position
                gradient_x: float = sub_matrix_x.apply_filter(
                    differential_filter).get_sum()
                gradient_y: float = sub_matrix_y.apply_filter(
                    differential_filter.transpose()).get_sum()
                gradient_absolute: int = int(
                    (abs(gradient_x) ** 2 + abs(gradient_y) ** 2) ** 0.5)

                pixels_differentiated[row_count].append(Pixel(
                    gradient_absolute, gradient_absolute, gradient_absolute))

        return pixels_differentiated
