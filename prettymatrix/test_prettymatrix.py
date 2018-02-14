import numpy as np
import unittest

from prettymatrix import prettymatrix


class PrintTest(unittest.TestCase):

    def test_empty_matrix(self):
        expected = (
            "┌  ┐\n"
            "└  ┘"
        )
        actual = prettymatrix.matrix_to_string(np.full((0, 0), ''))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
