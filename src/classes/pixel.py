"""File containing the Pixel class."""

class Pixel:
    """
    A class representing one Pixel.

    Attributes
    ----------
    red_value: float
        Value of the primary colour red.
    green_value: float
        Value of the primary colour green.
    blue_value: float
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

    def __init__(self, red_value: float, green_value: float, blue_value: float) -> None:
        """
        Initialize one Pixel object with the given attributes.

        Parameters
        ----------
        red_value: float
            Value of the primary colour red.
        green_value: float
            Value of the primary colour green.
        blue_value: float
            Value of the primary colour blue.

        """
        self.red_value: float = red_value
        self.green_value: float = green_value
        self.blue_value: float = blue_value

        # Determine the grey value of the pixel
        self.grey_value: int = int(
            sum([self.red_value * 0.2989, self.green_value * 0.5870,
                 self.blue_value * 0.1140]))

    def get_gray_value(self) -> int:
        """
        Return the grey value of the pixel.

        Returns
        -------
        self.grey_value: float
            Grey value of the pixel.

        """
        return self.grey_value

    def get_rgb_values(self) -> tuple[float, float, float]:
        """
        Return the RGB values of the image as a tuple.

        Returns
        -------
        self.red_value, self.green_value, self.blue_value: tuple[float, float, float]
            RGB values of the image as a tuple.

        """
        return (self.red_value, self.green_value, self.blue_value)
