"""File containing the matrix class."""

from __future__ import annotations

class Matrix:
    """
    A class representing one matrix.

    Attributes
    ----------
    values: list[list[float]]
        Values stored in the matrix.

    Methods
    -------
    get_values
        Return the values stored in the matrix.
    set_values
        Set the values of the matrix.
    get_number_of_rows
        Return the number of rows.
    get_number_of_columns
        Return the number of columns.
    get_value_at
        Return the value at the specified position.
    matrix_all_rows_same_length
        Check whether all rows of a given matrix have the same length.
    is_matrix
        Check if given values represent a matrix.
    matrix_multiplication
        Multiplicate two given matrices.
    transpose
        Transpose the matrix and return the values as a new matrix.
    get_sum
        Add all values of a matrix together and return it.
    apply_filter
        Apply a filter to each value of a matrix.
    two_matrices_same_dimensions
        Check whether two matrices have the same dimensions.
    create_sub_matrix
        Create a matrix including the pixel and the 8 surrounding pixels.

    """

    def __init__(self, values: list[list[float]]) -> None:
        """
        Construct one Matrix object with the given argument.

        Parameters
        ----------
        values: list[list[float]]
            Values stored in the matrix.

        """
        self.set_values(values)

        if not self.is_matrix():
            raise TypeError("Matrix can only contain numbers.")

        if not self.matrix_all_rows_same_length():
            raise TypeError("All rows must have the same length.")

    def get_values(self) -> list[list[float]]:
        """
        Return the values stored in the matrix.

        Returns
        -------
        self.values: list[list[float]]
            Values stored in the matrix.

        """
        return self.values

    def set_values(self, values: list[list[float]]) -> None:
        """
        Set the values of the matrix.

        Parameters
        ----------
        values: list[list[float]]
            Values stored in the matrix.

        """
        self.values = values

    def get_number_of_rows(self) -> int:
        """
        Return the number of rows.

        Returns
        -------
        len(self.get_values()): int
            Number of rows.

        """
        return len(self.get_values())

    def get_number_of_columns(self) -> int:
        """
        Return the number of columns.

        Returns
        -------
        len(self.get_values()[0]): int
            Number of columns.

        """
        return len(self.get_values()[0])

    def get_value_at(self, row: int, column: int) -> float:
        """
        Return the value at the specified position.

        Parameters
        ----------
        row: int
            Row of the value.
        column: int
            Column of the value.

        Returns
        -------
        self.values[row][column]: float
            Specified value.

        Raises
        ------
        IndexError
            If either the row or the column are not in range of the dimensions
            of the matrix.

        """
        if row not in range(0, self.get_number_of_rows()):
            raise IndexError("Row value out of range.")
        if column not in range(0, self.get_number_of_columns()):
            raise IndexError("Column value out of range.")

        return self.get_values()[row][column]

    def matrix_all_rows_same_length(self) -> bool:
        """
        Check whether all rows of a given matrix have the same length.

        Returns
        -------
        bool
            True if all rows have the same length, otherwise False.

        """
        # Get the length of the first line
        row_length: int = self.get_number_of_columns()

        # Check for all other lines if they have the same length as the first one
        for i in range(1, self.get_number_of_rows()):
            if row_length != len(self.get_values()[i]):
                return False

        return True

    def is_matrix(self) -> bool:
        """
        Check if given values represent a matrix.

        Returns
        -------
        bool
            Returns True if given values are a matrix, otherwise returns False.

        """
        for row in self.get_values():
            if not isinstance(row, list):
                return False

            for value in row:
                if not isinstance(value, (int, float)):
                    return False

        return True

    def transpose(self) -> Matrix:
        """
        Transpose the matrix and return the values as a new matrix.

        Returns
        -------
        matrix_inverted: Matrix
            Matrix with inverted values.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'Matrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        original_values: list[list[float]] = self.get_values()
        values_inverted: list[list[float]] = []

        for col in range(self.get_number_of_columns()):
            # For each column add a new row
            values_inverted.append([])

            for row in range(self.get_number_of_rows()):
                values_inverted[col].append(original_values[row][col])

        # Create and return the inverted matrix
        matrix_inverted: Matrix = Matrix(values_inverted)

        return matrix_inverted

    def get_sum(self) -> float:
        """
        Add all values of a matrix together and return it.

        Returns
        -------
        sum_matrix: float
            Sum of all values in the matrix.

        """
        # Initialize the return value
        sum_matrix: float = 0

        for row in self.get_values():
            for value in row:
                sum_matrix += value

        return sum_matrix

    def apply_filter(self, matrix_filter: Matrix) -> Matrix:
        """
        Apply a filter to each value of a matrix.

        Each value of the matrix is multiplicated with the respective value
        in the filter.

        Parameters
        ----------
        matrix_filter: Matrix
            To be applied filter with the same dimensions of the matrix.

        Returns
        -------
        new_values: Matrix
            Matrix values with the filter applied as an object of the Matrix class.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'Matrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Get the values of the two matrices
        values_matrix = self.get_values()
        values_filter = matrix_filter.get_values()

        # Initialize the return value
        new_values: list[list[float]] = []

        for row in range(len(values_matrix)):
            new_values.append([])

            for col in range(len(values_matrix[0])):
                new_values[row].append(
                    values_matrix[row][col] * values_filter[row][col])

        return Matrix(new_values)

    @staticmethod
    def two_matrices_same_dimensions(matrix_1: Matrix, matrix_2: Matrix) -> bool:
        """
        Check whether two matrices have the same dimensions.

        Parameters
        ----------
        matrix_1: Matrix
            First matrix of the check.
        matrix_2: Matrix
            Second matrix of the check.

        Returns
        -------
        bool
            Returns True when the two matrices have the same dimensions,
            otherwise returns False.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'Matrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        return (matrix_1.get_number_of_rows() == matrix_2.get_number_of_rows() and
                matrix_1.get_number_of_columns() == matrix_2.get_number_of_columns())

    def create_sub_matrix(self, pos: tuple[int, int], size: tuple[int, int]) -> Matrix:
        """
        Create a matrix including the pixel and the 8 surrounding pixels.

        Parameters
        ----------
        pos: tuple[int, int]
            Position of the pixel in the format of (row, column).
        size: tuple[int, int]
            Size that the sub matrix shall have. (Number of rows, Number of columns)

        Returns
        -------
        sub_matrix: Matrix
            Matrix containing the pixel and the 8 surrounding pixel.

        """
        # Get the values of the matrix
        values: list[list[float]] = self.get_values()

        # Get the indices for the height and width
        height: int = int(size[0] / 2)
        width: int = int(size[1] / 2)

        sub_matrix: Matrix = Matrix([
            [values[row][col] for col in range(pos[1] - width, pos[1] + width + 1)]
            for row in range(pos[0] - height, pos[0] + height + 1)])

        return sub_matrix
