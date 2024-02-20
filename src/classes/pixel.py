"""File containing the Pixel class."""

class Pixel:
    """
    A class representing one Pixel.

    Attributes
    ----------
    red_value: int
        Value of the primary colour red.
    green_value: int
        Value of the primary colour green.
    blue_value: int
        Value of the primary colour blue.
    grey_value: int
        Grey value of the pixel.

    Methods
    -------
    get_gray_value
        Return the grey value of the pixel.
    get_rgb_values
        Return the RGB values of the image as a tuple.

    """

    def __init__(self, red_value: int, green_value: int, blue_value: int) -> None:
        """
        Initialize one Pixel object with the given attributes.

        Paramneters
        -----------
        red_value: int
            Value of the primary colour red.
        green_value: int
            Value of the primary colour green.
        blue_value: int
            Value of the primary colour blue.

        """
        self.red_value: int = red_value
        self.green_value: int = green_value
        self.blue_value: int = blue_value

        # Determine the grey value of the pixel
        self.grey_value: int = int(sum([
            self.green_value, self.blue_value, self.green_value]) / 3)

    def get_gray_value(self) -> int:
        """
        Return the grey value of the pixel.

        Returns
        -------
        self.grey_value: int
            Grey value of the pixel.

        """
        return self.grey_value

    def get_rgb_values(self) -> tuple[int, int, int]:
        """
        Return the RGB values of the image as a tuple.

        Returns
        -------
        self.red_value, self.green_value, self.blue_value: tuple[int, int, int]
            RGB values of the image as a tuple.

        """
        return (self.red_value, self.green_value, self.blue_value)
