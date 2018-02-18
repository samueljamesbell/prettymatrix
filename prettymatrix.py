import itertools

import numpy as np


_PAD = ' ' 
_TOP_LEFT_CORNER = '┌'
_TOP_RIGHT_CORNER = '┐'
_BOTTOM_LEFT_CORNER = '└'
_BOTTOM_RIGHT_CORNER = '┘'
_BORDER = '│'

_ELLIPSIS = '…'

_MAX_HEIGHT = _MAX_WIDTH = 10
_SHRUNK_NUM_ROWS = _SHRUNK_NUM_COLS = 3


def matrix_to_string(M, name=None, include_dimensions=False):
    """Stringify a 2D matrix, M."""
    return _render(_format_matrix(M, name, include_dimensions))


def matrices_to_string(*seq):
    """Stringify a sequence of 2D matrices."""
    formatted = [_format_matrix(M) for M in seq]
    num_rows = max(M.shape[0] for M in formatted)
    padded = [_pad_horizontally(M, top_padding=0, bottom_padding=num_rows - M.shape[0]) for M in formatted]
    widths = [M.shape[1] for M in padded]
    return _render(_space_columns(np.concatenate(padded, axis=1), widths)) 


def _format_matrix(M, name=None, include_dimensions=False):
    """Return a copy of M with all formatting steps applied.

    This includes:
    * Split the contents of every cell to contain at most one character
    * Add a column of padding between every two columns
    * Wrap the entire matrix in padding
    * Add typical matrix-notation bracketing
    * Replace internal rows and columns with ellipses if matrix is too large
    * Optionally append a name row to the matrix
    * Optionally append a row containing the matrix's dimensions
    """
    N = _append_string_row(
            _border(
            _pad(
            _space_columns(
            *_normalize_all_cells(
            _cells_to_string(
            _cap_dimensions(M)))))), name)

    if include_dimensions:
        N = _append_string_row(N, '({}x{})'.format(*M.shape))

    return N


def _character_cell(c):
    """Return a (1x1) array wrapping character c."""
    return np.full((1,1), c)


def _character_column(c, height, width=1):
    """Return a column of fixed height filled with character c."""
    return np.full((height, width), c)


def _character_row(c, width, height=1):
    """Return a row of fixed width filled with character c."""
    return np.full((height, width), c)


def _left_border(M):
    """Build a left-hand border that would fit a matrix, M."""
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
    """Build a right-hand border that would fit a matrix, M."""
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
    """Return a copy of M wrapped in the convention matrix brackets."""
    left_border = _left_border(M)
    right_border = _right_border(M)

    bordered = np.concatenate((left_border, M, right_border), axis=1)

    return bordered


def _pad_vertically(M, left_padding=1, right_padding=1):
    """Return a copy of M wrapped on each side by columns of padding."""
    num_rows, num_cols = M.shape
    left_pad = _character_column(_PAD, num_rows, left_padding)
    right_pad = _character_column(_PAD, num_rows, right_padding)

    padded = np.concatenate(
         (left_pad,
          M,
          right_pad), axis=1)

    return padded


def _pad_horizontally(M, top_padding=1, bottom_padding=1):
    """Return a copy of M wrapped on the top and bottom by a single row of padding."""
    num_rows, num_cols = M.shape

    top_pad = _character_row(_PAD, num_cols, top_padding)
    bottom_pad = _character_row(_PAD, num_cols, bottom_padding)

    padded = np.concatenate(
        (top_pad,
         M,
         bottom_pad),
        axis=0)

    return padded


def _pad(M):
    """Return a copy of M wrapped by a single layer of padding on all sides."""
    return _pad_vertically(_pad_horizontally(M))


def _normalize_cell_width(M, min_column_width=0):
    """Return a cell with its contents normalized.

    See _normalize_all_cells for a description of normalization.

    Note that M should be a matrix of size (1x1).
    """
    split = np.concatenate([_character_cell(c) for c in M[0,0]], axis=1)
    right_padding_size = max(0, min_column_width - split.shape[1])
    right_padding = _character_row(_PAD, right_padding_size)
    return np.concatenate((split, right_padding), axis=1)
    

def _normalize_column_width(M, min_column_width=0):
    """Return a column where every cell has had its contents normalized.

    See _normalize_all_cells for a description of normalization.

    Note that M should be a column vector, that is, of size (nx1).
    """
    return np.concatenate([_normalize_cell_width(M[i:i+1, :], min_column_width)
                           for i in range(0, M.shape[0])], axis=0)


def _normalize_all_cells(M):
    """Return a matrix where every cell has had its contents normalized.

    By normalized, we mean that every cell containing a string s of length n,
    is split into n cells, each containing a single character of s.
    """
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
    """Return a matrix with a column of whitespace between every column in M."""
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
    """Return a matrix where every cell of M has been stringified."""
    return M.astype(str)


def _append_string_row(M, string):
    """Append a new row containing string to the bottom of the matrix."""
    if not string:
        return M

    num_rows, num_cols = M.shape
    string_row = _normalize_cell_width(np.array([[string]]), num_cols)
    right_padding = string_row.shape[1] - num_cols
    padded = _pad_vertically(M, 0, right_padding)
    return np.concatenate((padded, string_row), axis=0)


def _cap_dimensions(M):
    """Return a copy of M bounded to a fixed size.

    We keep a fixed number of the original columns and rows, but replace all
    the internals with ellipses to indicate omission.
    """
    return _cap_width(_cap_height(M))


def _cap_height(M):
    """Return a copy of M bounded to a fixed number of rows."""
    num_rows, num_cols = M.shape

    if num_rows <= _MAX_HEIGHT:
        return M

    top_segment = M[:_SHRUNK_NUM_ROWS, :]
    middle_segment = _character_row(_ELLIPSIS, num_cols, height=_SHRUNK_NUM_ROWS)
    bottom_segment = M[-_SHRUNK_NUM_ROWS:, :]

    return np.concatenate(
            (top_segment,
             middle_segment,
             bottom_segment), axis=0)


def _cap_width(M):
    """Return a copy of M bounded to a fixed number of columns."""
    num_rows, num_cols = M.shape

    if num_cols <= _MAX_WIDTH:
        return M

    top_segment = M[:, :_SHRUNK_NUM_COLS]
    middle_segment = _character_column(_ELLIPSIS, num_rows, width=_SHRUNK_NUM_COLS)
    bottom_segment = M[:, -_SHRUNK_NUM_COLS:]

    return np.concatenate(
            (top_segment,
             middle_segment,
             bottom_segment), axis=1)


def _render(M):
    """Return a string representation of the matrix, M."""
    return '\n'.join((''.join(row) for row in M))
