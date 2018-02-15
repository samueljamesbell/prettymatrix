import itertools

import numpy as np


_PAD = ' ' 
_TOP_LEFT_CORNER = '┌'
_TOP_RIGHT_CORNER = '┐'
_BOTTOM_LEFT_CORNER = '└'
_BOTTOM_RIGHT_CORNER = '┘'
_BORDER = '│'


def _character_cell(c):
    return np.full((1,1), c)


def _character_column(c, height, width=1):
     return np.full((height, width), c)


def _character_row(c, width):
     return np.full((1, width), c)


def _left_border(M):
    num_rows, num_cols = M.shape

    top_left_corner = _character_cell(_TOP_LEFT_CORNER)
    border = _character_column(_BORDER, num_rows - 2)
    bottom_left_corner = _character_cell(_BOTTOM_LEFT_CORNER)

    left_border = np.concatenate(
        (top_left_corner,
         border,
         bottom_left_corner),
        axis=0)

    return left_border


def _right_border(M):
    num_rows, num_cols = M.shape

    top_right_corner = _character_cell(_TOP_RIGHT_CORNER)
    border = _character_column(_BORDER, num_rows - 2)
    bottom_right_corner = _character_cell(_BOTTOM_RIGHT_CORNER)

    right_border = np.concatenate(
        (top_right_corner,
         border,
         bottom_right_corner),
        axis=0)

    return right_border


def _border(M):
    left_border = _left_border(M)
    right_border = _right_border(M)

    bordered = np.concatenate((left_border, M, right_border), axis=1)

    return bordered


def _pad_vertically(M, left_padding=1, right_padding=1):
    num_rows, num_cols = M.shape
    left_padding = _character_column(_PAD, num_rows, left_padding)
    right_padding = _character_column(_PAD, num_rows, right_padding)

    padded = np.concatenate(
         (left_padding,
          M,
          right_padding), axis=1)

    return padded


def _pad_horizontally(M):
    num_rows, num_cols = M.shape
    pad_row = _character_row(_PAD, num_cols)

    padded = np.concatenate(
        (pad_row,
         M,
         pad_row),
        axis=0)

    return padded


def _pad(M):
    return _pad_vertically(_pad_horizontally(M))


def _normalize_cell_width(M, min_column_width=0):
    split = np.concatenate([_character_cell(c) for c in M[0,0]], axis=1)
    right_padding_size = max(0, min_column_width - split.shape[1])
    right_padding = _character_row(_PAD, right_padding_size)
    return np.concatenate((split, right_padding), axis=1)
    

def _normalize_column_width(M, min_column_width=0):
    # M is a column vector
    return np.concatenate([_normalize_cell_width(M[i:i+1, :], min_column_width)
                           for i in range(0, M.shape[0])], axis=0)


def _normalize_all_cells(M):
    if M.shape == (0, 0):
        # Bit of a hack because we can't apply vectorized operations to 0x0
        # matrices.
        return M, np.full((0,0), 0)

    max_column_widths = np.max(np.vectorize(len)(M), axis=0)

    if M.shape[1] == 1:
        return _normalize_column_width(M, max_column_widths[0]), max_column_widths

    columns = np.split(M, M.shape[1], axis=1)
    zipped = zip(columns, max_column_widths)

    return np.concatenate([_normalize_column_width(col, w) for col, w in zipped],
                          axis=1), max_column_widths


def _space_columns(M, column_widths):
    if len(column_widths) == 1:
        return M

    num_rows, _ = M.shape

    indices = np.cumsum(column_widths)[:-1]
    columns = np.split(M, indices, axis=1)
    spacers = [_character_column(_PAD, num_rows)] * (len(columns) - 1)

    columns_with_spacers = [col for cols in itertools.zip_longest(columns, spacers)
                            for col in cols if col is not None]

    return np.concatenate(columns_with_spacers, axis=1)


def _cells_to_string(M):
    return M.astype(str)


def _append_string_row(M, name):
    if not name:
        return M

    num_rows, num_cols = M.shape
    name_row = _normalize_cell_width(np.array([[name]]), num_cols)
    right_padding = name_row.shape[1] - num_cols
    padded = _pad_vertically(M, 0, right_padding)
    return np.concatenate((padded, name_row), axis=0)


def _render(M):
    return '\n'.join((''.join(row) for row in M))



def matrix_to_string(M, name=None, include_dimensions=False):
    """Print a 2D matrix, M.
    
    e.g. 

    ┌     ┐
    │ 1 3 │
    │ 2 4 │
    └     ┘
     M_x
     (2x2)

    """
    N = _append_string_row(
            _border(
            _pad(
            _space_columns(
            *_normalize_all_cells(
            _cells_to_string(M))))), name)

    if include_dimensions:
        N = _append_string_row(N, '({}x{})'.format(*M.shape))

    return _render(N)
