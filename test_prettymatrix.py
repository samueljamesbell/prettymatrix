import unittest

import numpy as np

import prettymatrix


class MatrixToStringTest(unittest.TestCase):

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

    def test_empty_matrix_with_dimensions(self):
        expected = (
            "┌  ┐ \n"
            "└  ┘ \n"
            "(0x0)"
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''),
                                               include_dimensions=True)
        self.assertEqual(expected, actual)

    def test_1_x_1_matrix_with_dimensions(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "└   ┘\n"
            "(1x1)"
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 1), '0'),
                                               include_dimensions=True)
        self.assertEqual(expected, actual)

    def test_1_x_2_matrix_with_dimensions(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "└     ┘\n"
            "(1x2)  "
        )
        actual = prettymatrix.matrix_to_string(np.full((1, 2), '0'),
                                               include_dimensions=True)
        self.assertEqual(expected, actual)

    def test_2_x_1_matrix_with_dimensions(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "└   ┘\n"
            "(2x1)"
        )
        actual = prettymatrix.matrix_to_string(np.full((2, 1), '0'),
                                               include_dimensions=True)
        self.assertEqual(expected, actual)

    def test_empty_matrix_with_name_and_dimensions(self):
        expected = (
            "┌  ┐ \n"
            "└  ┘ \n"
            "M    \n"
            "(0x0)"
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''),
                                               name='M',
                                               include_dimensions=True)
        self.assertEqual(expected, actual)

    def test_10x1_matrix_renders_normally(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "└   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((10,1), '0'))
        self.assertEqual(expected, actual)

    def test_11x1_matrix_inserts_ellipses(self):
        expected = (
            "┌   ┐\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ … │\n"
            "│ … │\n"
            "│ … │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "│ 0 │\n"
            "└   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((11,1), '0'))
        self.assertEqual(expected, actual)

    def test_11x2_matrix_inserts_ellipses(self):
        expected = (
            "┌     ┐\n"
            "│ 0 0 │\n"
            "│ 0 0 │\n"
            "│ 0 0 │\n"
            "│ … … │\n"
            "│ … … │\n"
            "│ … … │\n"
            "│ 0 0 │\n"
            "│ 0 0 │\n"
            "│ 0 0 │\n"
            "└     ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((11,2), '0'))
        self.assertEqual(expected, actual)

    def test_1x10_matrix_renders_normally(self):
        expected = (
            "┌                     ┐\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "└                     ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((1,10), '0'))
        self.assertEqual(expected, actual)

    def test_1x10_matrix_inserts_ellipses(self):
        expected = (
            "┌                   ┐\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "└                   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((1,11), '0'))
        self.assertEqual(expected, actual)

    def test_10x10_matrix_renders_normally(self):
        expected = (
            "┌                     ┐\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "│ 0 0 0 0 0 0 0 0 0 0 │\n"
            "└                     ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((10,10), '0'))
        self.assertEqual(expected, actual)

    def test_11x11_matrix_inserts_ellipses(self):
        expected = (
            "┌                   ┐\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "│ … … … … … … … … … │\n"
            "│ … … … … … … … … … │\n"
            "│ … … … … … … … … … │\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "│ 0 0 0 … … … 0 0 0 │\n"
            "└                   ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((11,11), '0'))
        self.assertEqual(expected, actual)


class MatricesToStringTest(unittest.TestCase):

    def test_two_empty_matrices(self):
        expected = (
            "┌  ┐ ┌  ┐\n"
            "└  ┘ └  ┘"
        )
        actual = prettymatrix.matrices_to_string(np.full((0, 0), ''), np.full((0, 0), ''))
        self.assertEqual(expected, actual)

    def test_two_1x1_matrices(self):
        expected = (
            "┌   ┐ ┌   ┐\n"
            "│ 0 │ │ 0 │\n"
            "└   ┘ └   ┘"
        )
        actual = prettymatrix.matrices_to_string(np.full((1, 1), '0'), np.full((1, 1), '0'))
        self.assertEqual(expected, actual)

    def test_different_width_matrices(self):
        expected = (
            "┌   ┐ ┌     ┐\n"
            "│ 0 │ │ 0 0 │\n"
            "└   ┘ └     ┘"
        )
        actual = prettymatrix.matrices_to_string(np.full((1, 1), '0'), np.full((1, 2), '0'))
        self.assertEqual(expected, actual)

    def test_different_height_matrices(self):
        expected = (
            "┌   ┐ ┌   ┐\n"
            "│ 0 │ │ 0 │\n"
            "└   ┘ │ 0 │\n"
            "      └   ┘"
        )
        actual = prettymatrix.matrices_to_string(np.full((1, 1), '0'), np.full((2, 1), '0'))
        self.assertEqual(expected, actual)

    def test_different_height_matrices_mirror(self):
        expected = (
            "┌   ┐ ┌   ┐\n"
            "│ 0 │ │ 0 │\n"
            "│ 0 │ └   ┘\n"
            "└   ┘      "
        )
        actual = prettymatrix.matrices_to_string(np.full((2, 1), '0'), np.full((1, 1), '0'))
        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()
