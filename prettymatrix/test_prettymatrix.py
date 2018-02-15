import unittest

import numpy as np

from prettymatrix import prettymatrix


class PrettyMatrixTest(unittest.TestCase):

    def test_empty_matrix(self):
        expected = (
            "┌  ┐\n"
            "└  ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''))
        self.assertEqual(expected, actual)

    def test_1_x_1_matrix(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "└   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 1), '0'))
        self.assertEqual(expected, actual)

    def test_2_x_1_matrix(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "└   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((2, 1), '0'))
        self.assertEqual(expected, actual)

    def test_1_x_1_matrix_with_multi_digit_cell(self):
        expected = (
            "┌    ┐\n"
            "│ 00 │\n"
            "└    ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 1), '00'))
        self.assertEqual(expected, actual)

    def test_2_x_1_matrix_with_multi_digit_cells(self):
        expected = (
            "┌    ┐\n"
            "│ 00 │\n"
            "│ 00 │\n"
            "└    ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((2, 1), '00'))
        self.assertEqual(expected, actual)

    def test_2_x_1_matrix_with_single_and_multi_digit_cells(self):
        expected = (
            "┌    ┐\n"
            "│ 0  │\n"
            "│ 00 │\n"
            "└    ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['0'], ['00']]))
        self.assertEqual(expected, actual)

    def test_2_x_1_matrix_with_multi_and_single_digit_cells(self):
        expected = (
            "┌    ┐\n"
            "│ 00 │\n"
            "│ 0  │\n"
            "└    ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00'], ['0']]))
        self.assertEqual(expected, actual)

    def test_1_x_2_matrix_with_single_digit_cells(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "└     ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 2), '0'))
        self.assertEqual(expected, actual)

    def test_1_x_2_matrix_with_single_and_multi_digit_cells(self):
        expected = (
            "┌      ┐\n"
            "│ 00 0 │\n"
            "└      ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '0']]))
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_single_digit_cells(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "│ 0 0 │\n"
            "└     ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((2,2), '0'))
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_single_and_multi_digit_cells(self):
        expected = (
            "┌      ┐\n"
            "│ 00 0 │\n"
            "│ 0  0 │\n"
            "└      ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '0'], ['0', '0']]))
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_single_and_multi_digit_cells_2(self):
        expected = (
            "┌      ┐\n"
            "│ 00 0 │\n"
            "│ 00 0 │\n"
            "└      ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '0'], ['00', '0']]))
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_single_and_multi_digit_cells_3(self):
        expected = (
            "┌       ┐\n"
            "│ 00 00 │\n"
            "│ 0  0  │\n"
            "└       ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '00'], ['0', '0']]))
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_single_and_multi_digit_cells_4(self):
        expected = (
            "┌        ┐\n"
            "│ 00 000 │\n"
            "│ 0  00  │\n"
            "└        ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '000'], ['0', '00']]))
        self.assertEqual(expected, actual)

    def test_empty_matrix_with_short_name(self):
        expected = (
            "┌  ┐\n"
            "└  ┘\n"
            "W   "
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''), name='W')
        self.assertEqual(expected, actual)

    def test_empty_matrix_with_long_name(self):
        expected = (
            "┌  ┐ \n"
            "└  ┘ \n"
            "W_x_y"
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''), name='W_x_y')
        self.assertEqual(expected, actual)

    def test_1_x_1_matrix_with_short_name(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "└   ┘\n"
            "W    "
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 1), '0'), name='W')
        self.assertEqual(expected, actual)

    def test_1_x_1_matrix_with_long_name(self):
        expected = (
            "┌   ┐  \n"
            "│ 0 │  \n"
            "└   ┘  \n"
            "W_x_y_z"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 1), '0'),
                                               name='W_x_y_z')
        self.assertEqual(expected, actual)

    def test_1_x_2_matrix_with_short_name(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "└     ┘\n"
            "W      "
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 2), '0'), name='W')
        self.assertEqual(expected, actual)

    def test_1_x_2_matrix_with_long_name(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "└     ┘\n"
            "W_x_y_z"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 2), '0'),
                                               name='W_x_y_z')
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_short_name(self):
        expected = (
            "┌        ┐\n"
            "│ 00 000 │\n"
            "│ 0  00  │\n"
            "└        ┘\n"
            "W         "
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '000'], ['0', '00']]),
                                               name='W')
        self.assertEqual(expected, actual)

    def test_2_x_2_matrix_with_long_name(self):
        expected = (
            "┌        ┐ \n"
            "│ 00 000 │ \n"
            "│ 0  00  │ \n"
            "└        ┘ \n"
            "W_long_name"
        )
        actual = prettymatrix.matrix_to_string(np.array([['00', '000'], ['0', '00']]),
                                               name='W_long_name')
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
