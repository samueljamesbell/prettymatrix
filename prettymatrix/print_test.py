import numpy as np
import unittest

from prettymatrix import prettymatrix


class PrettyMatrixTest(unittest.TestCase):

    def test_empty_matrix(self):
        expected = (
            "┌ ┐"
            "└ ┘"
        )
        actual = prettymatrix.matrix_to_string(np.array([[]]))
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
