"""File containing the matrix class."""

from __future__ import annotations

class Matrix:
    """
    A class representing one matrix.

    Attributes
    ----------
    values: list[list[int]]
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
    invert
        Invert the matrix and return the values as a new matrix.

    """

    def __init__(self, values: list[list[int]]) -> None:
        """
        Construct one Matrix object with the given argument.

        Parameters
        ----------
        values: list[list[int]]
            Values stored in the matrix.

        """
        self.set_values(values)

        if not self.is_matrix():
            raise TypeError("Matrix can only contain numbers.")

        if not self.matrix_all_rows_same_length():
            raise TypeError("All rows must have the same length.")

    def get_values(self) -> list[list[int]]:
        """
        Return the values stored in the matrix.

        Returns
        -------
        self.values: list[list[int]]
            Values stored in the matrix.

        """
        return self.values

    def set_values(self, values: list[list[int]]) -> None:
        """
        Set the values of the matrix.

        Parameters
        ----------
        values: list[list[int]]
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

    def get_value_at(self, row: int, column: int) -> int:
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
        self.values[row][column]: int
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
                if not isinstance(value, int):
                    return False

        return True

    @staticmethod
    def matrix_multiplication(matrix_1: Matrix, matrix_2: Matrix) -> Matrix:
        """
        Multiplicate two given matrices.

        Parameters
        ----------
        matrix_1: Matrix
            First matrix of the equation.
        matrix_2: Matrix
            Second matrix of the equation.

        Returns
        -------
        matrix_product: Matrix
            Product of the two given matrices.

        Raises
        ------
        ValueError
            If the number of columns of the first matrix is not equal to the number of
            rows of the second matrix.

        Notes
        -----
        Import in line 4 is necessary for type hints of this function as the type
        'Matrix' is used as a forward reference here (see index 563 of the
        Python Enhancement Proposals [PEP 563]).

        """
        # Check if the two given matrices can be multiplicated
        if matrix_1.get_number_of_columns() != matrix_2.get_number_of_rows():
            raise ValueError("The two given matrices can't be multiplicated.")

        # Initialize the product of the two given matrices
        matrix_product: list[list[int]] = []

        for row_matrix_1 in range(matrix_1.get_number_of_rows()):
            # Add a new line to the product.
            matrix_product.append([])

            for column_matrix_2 in range(matrix_2.get_number_of_columns()):
                # Multiply row of matrix 1 with column of matrix 2
                matrix_product[row_matrix_1].append(sum([
                    matrix_1.get_value_at(row_matrix_1, col_1_row_2)
                    * matrix_2.get_value_at(col_1_row_2, column_matrix_2)
                    for col_1_row_2 in range(matrix_1.get_number_of_columns())]))

        return Matrix(matrix_product)

    def invert(self) -> Matrix:
        """
        Invert the matrix and return the values as a new matrix.

        Returns
        -------
        matrix_inverted: Matrix
            Matrix with inverted values.

        """
        original_values: list[list[int]] = self.get_values()
        values_inverted: list[list[int]] = []

        for col in range(self.get_number_of_columns()):
            # For each column add a new row
            values_inverted.append([])

            for row in range(self.get_number_of_rows()):
                values_inverted[col].append(original_values[row][col])

        # Create and return the inverted matrix
        matrix_inverted: Matrix = Matrix(values_inverted)

        return matrix_inverted
