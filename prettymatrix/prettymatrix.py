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


def _character_column(c, height):
     return np.full((height, 1), c)


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


def _pad_vertically(M):
    num_rows, num_cols = M.shape
    pad_column = _character_column(_PAD, num_rows)

    padded = np.concatenate(
        (pad_column,
         M,
         pad_column),
        axis=1)

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


def _render(M):
    return '\n'.join((''.join(row) for row in M))



def matrix_to_string(M, name=None, include_dimensions=False):
    """Print a 2D matrix, M.
    
    e.g. 

      x 2 
      2 ┌     ┐
        │ 1 3 │
        │ 2 4 │
        └     ┘
          M_x

    """
    return _render(_border(_pad(_space_columns(*_normalize_all_cells(_cells_to_string(M))))))


#    name = name or ''
#
#    num_rows, num_cols = M.shape
#
#    cell_lengths = np.vectorize(len)(M.astype(str))
#    row_lengths = cell_lengths.sum(axis=0)
#    between_cell_padding = num_cols - 1 
#
#    # 4 is the width of row's border and single space internal padding
#    # There are 2 empty spaces to the left of a name
#    row_widths = 4 + between_cell_padding + row_lengths
#    padded_name_length = len((2 * _PAD) + name)
#
#    right_of_cell_paddings = _PAD * (padded_name_length - max(row_widths))
#
#
#    desired_column_width = cell_lengths.max(axis=0)
#
#    padded_cells = np.empty_like(M)
#    for i, row in enumerate(M.astype(str)):
#        for j, cell in enumerate(row):
#            padded_cells[i][j] = cell.ljust(desired_column_width[j], _PAD)
#
#    middle_rows = ['│ {} │{}'.format(_PAD.join([str(x) for x in row]),
#                                              right_of_cell_paddings)
#                                     for row in padded_cells]
#
#    num_rows, num_cols = M.shape
#    max_row_length = max(len(r) for r in middle_rows)
#    top_row = ['┌ {} ┐{}'.format(' ' * (max_row_length - 4),
#        right_of_cell_paddings)]
#    bottom_row = ['└ {} ┘{}'.format(' ' * (max_row_length - 4),
#        right_of_cell_paddings)]
#    matrix = '\n'.join(top_row + middle_rows + bottom_row)
#    print(matrix)

#    if name:
#        name_line = '  {}'.format(name)
#        print(len(name_line))
#        print(max_row_length)
#        if len(name_line) > max_row_length:
#            right_padding = '-'  * (len(name_line) - max_row_length)
#
#            for row in enumerate(matrix):
#                row += right_padding
#
#        matrix += '\n' + name_line 
#
#    return matrix

#matrix_to_string(np.array([[1, np.tanh], [2, 3], [3, 3]]))
#matrix_to_string(np.array([[1], [2], [3]]))
#matrix_to_string(np.array([[1]]), name='W_x_y')

## Column vector, and 2D matrices
#print(matrix_to_string(np.array([[1], [2], [3]])))
#print(matrix_to_string(np.array([[1, 2, 3]])))
#print(matrix_to_string(np.array([[1, 2, 3], [1, 2, 3]])))
#
## Single-letter name labels
#print(matrix_to_string(np.array([[1], [2], [3]]), 'M'))
#print(matrix_to_string(np.array([[1, 2, 3]]), 'M'))
#print(matrix_to_string(np.array([[1, 2, 3], [1, 2, 3]]), 'M'))
#
## Multi-letter name labels
#print(matrix_to_string(np.array([[1], [2], [3]]), 'M_x'))
#print(matrix_to_string(np.array([[1], [2], [3]]), 'M_x_y_z'))
