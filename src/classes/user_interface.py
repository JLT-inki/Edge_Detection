"""File containing the UserInterface class."""

import os

from tkinter import Tk, Label, IntVar, Radiobutton, BooleanVar, Checkbutton
from PIL import ImageTk, Image

from classes.matrix import Matrix

class UserInterface:
    """
    A class representing one window of the user interface.

    Attributes
    ----------
    window: Tk
        Window in which the details are displayed in.
    name: str
        Title of the window.
    height:
        Height of the window.
    width:
        Width of the window.
    crossed_image: IntVar
        The image on which the filter(s) shall be applied.
    radio_buttons: list[Radiobutton]
        Buttons for the choosable images.
    crosses: list[BooleanVar]
        Booleans indicating which filter(s) shall be applied.
    checkboxes
        Checkboxes for the choosable filter(s)
    labels: list[Label]
        All displayed labels (text) on the window.
    images: list[ImageTk.PhotoImage]
        All displayed images on the window.

    Methods
    -------
    add_images
        Add the images to the window.
    add_filters
        Add the filters to the window.
    show_window
        Add the images and filter and show the window afterwards.

    Notes
    -----
    The lists are all used to store these objects in a variable as they
    would otherwise automatically be destroyed by the garbage collector.

    """

    def __init__(self, window: Tk, name: str, height: int, width: int) -> None:
        """
        Construct one UserInterface object with the given attributes.

        Parameters
        ----------
        window: Tk
            Window in which the details are displayed in.
        name: str
            Title of the window.
        height:
            Height of the window.
        width:
            Width of the window.

        """
        # Set the given attributes
        self.window: Tk = window
        self.name: str = name
        self.height: int = height
        self.width: int = width

        # Apply the height and width to the window
        self.window.geometry(str(height) + "x" + str(width))

        # Apply the title to the window
        self.window.title(self.name)

        # Initialize the other attributes of the object
        self.crossed_image: IntVar = IntVar()
        self.radio_buttons: list[Radiobutton] = []

        self.crosses: list[BooleanVar] = []
        self.checkboxes: list[Checkbutton] = []

        self.labels: list[Label] = []

        self.images: list[ImageTk.PhotoImage] = []

    def add_images(self, path_to_images: str, row: int, col: int) -> None:
        """
        Add the images to the window.

        Parameters
        ----------
        path_to_images: str
            Path to the image folder.
        row:
            Row of the grid where the images shall be placed.
        col:
            Column of the grid where the images shall be placed.

        """
        images: list[str] = os.listdir(path_to_images)

        label_images: Label = Label(
            self.window, text="Choose the Image:"
        ).grid(row=row, column=col, sticky="W")
        self.labels.append(label_images)

        for count, image in enumerate(images):
            photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(
                Image.open(path_to_images + image).resize((75, 75)))
            self.images.append(photo_image)

            radio_button: Radiobutton = Radiobutton(
                self.window, image=photo_image, indicatoron=False, bd=2,
                variable=self.crossed_image, value=count)
            radio_button.grid(row=(row + count + 1), column=col)
            self.radio_buttons.append(radio_button)

    def add_filters(self, filters: dict[str, Matrix], row: int,
                    col: int) -> None:
        """
        Add the filters to the window.

        Parameters
        ----------
        filters: dict[str, Matrix]
            The filters from which the user can choose.
        row:
            Row of the grid where the filters shall be placed.
        col:
            Column of the grid where the filters shall be placed.

        """
        label_filters: Label = Label(
            self.window, text="Choose the to be applied filter(s):"
        ).grid(row=row, column=col, sticky="W", columnspan=2)
        self.labels.append(label_filters)

        for count, key in enumerate(list(filters.keys())):
            cross: BooleanVar = BooleanVar()
            self.crosses.append(cross)

            checkbox: Checkbutton = Checkbutton(
                self.window, text=key, variable=cross
            ).grid(row=(row + count + 1), column=col, sticky="W")
            self.checkboxes.append(checkbox)

            label_matrix: Label = Label(
                self.window, text=filters[key].to_string(), justify="left",
                font=("Courier", 8)).grid(
                    row=(row + count + 1), column=(col + 1), sticky="W")
            self.labels.append(label_matrix)

        # Get the current row for further usage
        current_row: int = row + len(self.checkboxes) + 1

        # Add the standard checkbox for the original image
        cross_original: BooleanVar = BooleanVar(value=True)
        self.crosses.append(cross_original)

        checkbox_original: Checkbutton = Checkbutton(
            self.window, text="Original Image", variable=cross_original
        ).grid(row=current_row, column=col, sticky="W")
        self.checkboxes.append(checkbox_original)

        # Add the standard checkbox for the grayscale image
        cross_grayscale: BooleanVar = BooleanVar(value=True)
        self.crosses.append(cross_grayscale)

        checkbox_grayscale: Checkbutton = Checkbutton(
            self.window, text="Grayscale Image", variable=cross_grayscale
        ).grid(row=(current_row + 1), column=col, sticky="W")
        self.checkboxes.append(checkbox_grayscale)

    def show_window(self, filters: dict[str, Matrix], path_to_images: str) -> None:
        """
        Add the images and filter and show the window afterwards.

        filters: dict[str, Matrix]
            The filters from which the user can choose.
        path_to_images: str
            Path to the image folder.

        """
        # Add filters and images to the window
        self.add_filters(filters, 0, 0)
        self.add_images(path_to_images, 0, 2)

        # Show the window
        self.window.mainloop()
