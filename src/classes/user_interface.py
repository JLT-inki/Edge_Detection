"""File containing the UserInterface class."""

# Import for getting the contents of a folder
import os

# Import used components in the user interface
from tkinter import Tk, Label, IntVar, Radiobutton, BooleanVar, Checkbutton, Button

# Imports for reading images
from PIL import ImageTk, Image as ImageOpener

# Import to show the images
import matplotlib.pyplot as plt

# Import used classes
from classes.matrix import Matrix
from classes.image import Image

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
    status_label
        Label showing the current status of the program. By default, it shows
        nothing.
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
    buttons: list[Button]
        All regular buttons displayed on the window.

    Methods
    -------
    add_images
        Add the images to the window.
    add_filters
        Add the filters to the window.
    add_buttons
        Add the two buttons to the window.
    show_window
        Add the images and filter and show the window afterwards.
    execute_detection
        Execute the selected filters.
    close
        Close the window and therefore end the program.
    switch_buttons
        Enable/Disable all buttons on the window.
    update_status
        Update the status label on the window.

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
        self.window.geometry(str(width) + "x" + str(height))

        # Apply the title to the window
        self.window.title(self.name)

        # Initialize the label that shows error messages/ status of the program
        self.status_label: Label = Label(self.window, text="STATUS:", justify="left")
        self.status_label.grid(row=9, column=0, columnspan=3, sticky="W")

        # Initialize the other attributes of the object
        self.crossed_image: IntVar = IntVar()
        self.radio_buttons: list[Radiobutton] = []

        self.crosses: list[BooleanVar] = []
        self.checkboxes: list[Checkbutton] = []

        self.labels: list[Label] = []

        self.images: list[ImageTk.PhotoImage] = []

        self.buttons: list[Button] = []

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

        label_images: Label = Label(self.window, text="Choose the Image:")
        label_images.grid(row=row, column=col, sticky="W")
        self.labels.append(label_images)

        for count, image in enumerate(images):
            photo_image: ImageTk.PhotoImage = ImageTk.PhotoImage(
                ImageOpener.open(path_to_images + image).resize((75, 75)))
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
            self.window, text="Choose the to be applied filter(s):")
        label_filters.grid(row=row, column=col, sticky="W", columnspan=2)
        self.labels.append(label_filters)

        for count, key in enumerate(list(filters.keys())):
            cross: BooleanVar = BooleanVar()
            self.crosses.append(cross)

            checkbox: Checkbutton = Checkbutton(self.window, text=key, variable=cross)
            checkbox.grid(row=(row + count + 1), column=col, sticky="W")
            self.checkboxes.append(checkbox)

            label_matrix: Label = Label(self.window, text=filters[key].to_string(),
                                        justify="left", font=("Courier", 8))
            label_matrix.grid(row=(row + count + 1), column=(col + 1), sticky="W")
            self.labels.append(label_matrix)

        # Get the current row for further usage
        current_row: int = row + len(self.checkboxes) + 1

        # Add the standard checkbox for the original image
        cross_original: BooleanVar = BooleanVar(value=True)
        self.crosses.append(cross_original)

        checkbox_original: Checkbutton = Checkbutton(
            self.window, text="Original Image", variable=cross_original)
        checkbox_original.grid(row=current_row, column=col, sticky="W")
        self.checkboxes.append(checkbox_original)

        # Add the standard checkbox for the grayscale image
        cross_grayscale: BooleanVar = BooleanVar(value=True)
        self.crosses.append(cross_grayscale)

        checkbox_grayscale: Checkbutton = Checkbutton(
            self.window, text="Grayscale Image", variable=cross_grayscale)
        checkbox_grayscale.grid(row=(current_row + 1), column=col, sticky="W")
        self.checkboxes.append(checkbox_grayscale)

    def add_buttons(self, filters: dict[str, Matrix], path_to_images: str,
                    position: tuple[int, int]) -> None:
        """
        Add the two buttons to the window.

        One button is used to execute the selected filters on the selected image,
        whereas the other is used to the close the window and thereby exit the
        entire program.

        Parameters
        ----------
        position: tuple[int, int]
            Position of the first placed button. The position of the second button
            is also based on it.
        filters: dict[str, Matrix]
            The filters from which the user can choose.
        path_to_images: str
            Path to the image folder.

        """
        # Add the button to the execute the filters
        execution_button: Button = Button(
            self.window, text="Execute", width=8,
            command=lambda: self.execute_detection(filters, path_to_images))
        execution_button.place(x=position[0], y=position[1])
        self.buttons.append(execution_button)

        # Add the button to exit the program
        exit_button: Button = Button(
            self.window, text="Exit", command=self.close, width=8)
        exit_button.place(x=(position[0] + 70), y=position[1])
        self.buttons.append(exit_button)

    def show_window(self, filters: dict[str, Matrix], path_to_images: str) -> None:
        """
        Add the images and filter and show the window afterwards.

        filters: dict[str, Matrix]
            The filters from which the user can choose.
        path_to_images: str
            Path to the image folder.

        """
        # Add filters, images and buttons to the window
        self.add_filters(filters, 0, 0)
        self.add_images(path_to_images, 0, 2)
        self.add_buttons(filters, path_to_images, (450, 510))

        # Show the window
        self.window.mainloop()

    def execute_detection(self, filters: dict[str, Matrix],
                          path_to_images: str) -> None:
        """
        Execute the selected filters.

        Parameters
        ----------
        filters: dict[str, Matrix]
            The filters from which the user can choose.
        path_to_images: str
            Path to the image folder.

        Notes
        -----
        A check is performed to indicate whether a check box has been crossed. Usually
        this should not be a problem as by default the original image and the
        grayscale image is selected.
        The program does not check whether an image has been selected, since the
        car image is automatically selected and the implementation forces to always
        have one image selected.

        """
        # Check if any filter has been selected
        if not any(cross.get() for cross in self.crosses):
            self.update_status("ERROR!\tNo filter selected!")
        else:
            # Disable all buttons
            self.switch_buttons()

            # Create an Image object
            self.update_status("Create Image Object.")
            path_to_image: str = os.path.join(
                path_to_images + os.listdir(path_to_images)[self.crossed_image.get()])
            image: Image = Image.read_image(path_to_image)

            # Get the number of images to be shown
            number_of_images: int = [cross.get() for cross in self.crosses].count(True)

            # Get the number columns on the plot (By default there are two rows)
            cols: int = int(number_of_images / 2 if number_of_images % 2 == 0
                            else (number_of_images + 1) / 2)

            # Initialize the count of the image on the plot
            image_index: int = 1

            # Initialize the plot to show the images
            figure = plt.figure(figsize=(2, 2))
            # Check whether the original and/or the grayscale image shall be shown
            show_original: bool = self.crosses[-2].get()
            show_grayscale: bool = self.crosses[-1].get()

            if show_original:
                # Add the image to the plot
                self.update_status("Adding original image to the plot.")
                figure.add_subplot(2, cols, image_index)
                image.add_image_to_plot("Original Image")

                # Increment the image count
                image_index += 1
            if show_grayscale:
                # Add the image to the plot
                self.update_status("Adding grayscale image to the plot.")
                figure.add_subplot(2, cols, image_index)
                image.add_image_to_plot("Grayscale Image", grayscale=True)

                # Increment the image count
                image_index += 1

            # Apply the selected filters
            for count, key in enumerate(list(filters.keys())):
                if self.crosses[count].get():
                    # Apply the filter to the image
                    self.update_status("Applying " + key + " filter")
                    image_traversed = Image(image.traverse(filters[key]))

                    # Add the filtered image to the plot
                    self.update_status("Adding " + key + " filter to the plot.")
                    figure.add_subplot(2, cols, image_index)
                    image_traversed.add_image_to_plot(key + " filter")

                    # Increment the image count
                    image_index += 1

            # Show all images
            plt.show()

            # Reset the status message
            self.update_status("")

            # Enable all buttons
            self.switch_buttons()

    def close(self):
        """Close the window and therefore end the program."""
        self.window.destroy()

    def switch_buttons(self) -> None:
        """Enable/Disable all buttons on the window."""
        for button in self.buttons:
            # Enable the button if it is disabled and disable it otherwise
            if button['state'] == "disabled":
                button.config(state="normal")
            else:
                button.config(state="disabled")

    def update_status(self, text: str) -> None:
        """
        Update the status label on the window.

        Parameters
        ----------
        text: str
            To be displayed text on the label.

        """
        self.status_label.config(text="STATUS:\n" + text)
        self.status_label.update()
