import numpy as np


_PAD = ' ' 

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
    name = name or ''

    num_rows, num_cols = M.shape

    cell_lengths = np.vectorize(len)(M.astype(str))
    row_lengths = cell_lengths.sum(axis=0)
    between_cell_padding = num_cols - 1 

    # 4 is the width of row's border and single space internal padding
    # There are 2 empty spaces to the left of a name
    row_widths = 4 + between_cell_padding + row_lengths
    padded_name_length = len((2 * _PAD) + name)

    right_of_cell_paddings = _PAD * (padded_name_length - max(row_widths))


    desired_column_width = cell_lengths.max(axis=0)

    padded_cells = np.empty_like(M)
    for i, row in enumerate(M.astype(str)):
        for j, cell in enumerate(row):
            padded_cells[i][j] = cell.ljust(desired_column_width[j], _PAD)

    middle_rows = ['│ {} │{}'.format(_PAD.join([str(x) for x in row]),
                                              right_of_cell_paddings)
                                     for row in padded_cells]

    num_rows, num_cols = M.shape
    max_row_length = max(len(r) for r in middle_rows)
    top_row = ['┌ {} ┐{}'.format(' ' * (max_row_length - 4),
        right_of_cell_paddings)]
    bottom_row = ['└ {} ┘{}'.format(' ' * (max_row_length - 4),
        right_of_cell_paddings)]
    matrix = '\n'.join(top_row + middle_rows + bottom_row)
    print(matrix)

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

matrix_to_string(np.array([[1, np.tanh], [2, 3], [3, 3]]))
matrix_to_string(np.array([[1], [2], [3]]))
matrix_to_string(np.array([[1]]), name='W_x_y')

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
