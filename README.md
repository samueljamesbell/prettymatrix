prettymatrix
============

[![Build Status](https://travis-ci.org/samueljamesbell/prettymatrix.svg?branch=master)](https://travis-ci.org/samueljamesbell/prettymatrix)

Struggling to tell your rows from your columns?

`prettymatrix` creates human-friendly string representations of your numpy matrices and vectors, just like you're used
to.

Installation
------------
Available through pip:

```
pip install prettymatrix
```

Examples
--------
### Stringify a single matrix
```
import numpy as np
import prettymatrix

M = np.array([['1', '22'], ['333', '4444']])

print(prettymatrix.matrix_to_string(M))

# =>
#  ┌          ┐
#  │ 1   22   │
#  │ 333 4444 │
#  └          ┘
#

# We condense large matrices to a readable size
N = prettymatrix.matrix_to_string(np.full((1000,1000), '0'))

print(prettymatrix.matrix_to_string(N))

# =>
#  ┌                   ┐
#  │ 0 0 0 … … … 0 0 0 │
#  │ 0 0 0 … … … 0 0 0 │
#  │ 0 0 0 … … … 0 0 0 │
#  │ … … … … … … … … … │
#  │ … … … … … … … … … │
#  │ … … … … … … … … … │
#  │ 0 0 0 … … … 0 0 0 │
#  │ 0 0 0 … … … 0 0 0 │
#  │ 0 0 0 … … … 0 0 0 │
#  └                   ┘
#
```

Annotate your matrix with a name:

```
import numpy as np
import prettymatrix

M = np.array([['0'], ['0']])

print(prettymatrix.matrix_to_string(M, name='M_x_y'))

# =>
#  M_x_y
#  ┌   ┐
#  │ 0 │
#  │ 0 │
#  └   ┘
#
```

Or its dimensions:

```
import numpy as np
import prettymatrix

M = np.array([['0'], ['0']])

print(prettymatrix.matrix_to_string(M, include_dimensions=True))

# =>
#  (2x1)
#  ┌   ┐
#  │ 0 │
#  │ 0 │
#  └   ┘
#
```

### Stringify a multiple matrices in a row
```
import numpy as np
import prettymatrix

M = np.array([['1', '22'], ['333', '4444']])

print(prettymatrix.matrices_to_string(M, M))

# =>
#  ┌          ┐ ┌          ┐
#  │ 1   22   │ │ 1   22   │
#  │ 333 4444 │ │ 333 4444 │
#  └          ┘ └          ┘
#
```

### Stringify an expression containing matrices and operators
```
import numpy as np
import prettymatrix

M = np.array([['1', '1'], ['1', '1']])

print(prettymatrix.expression_to_string(M,
                                        prettymatrix.HADAMARD,
                                        M,
                                        prettymatrix.EQUALS,
                                        M,
                                        names=['M', 'M', 'M'),
                                        include_dimensions=True)

# =>
#  M         M         M
#  (2x2)     (2x2)     (2x2)
#  ┌     ┐ ∘ ┌     ┐ = ┌     ┐
#  │ 1 1 │   │ 1 1 │   │ 1 1 │
#  │ 1 1 │   │ 1 1 │   │ 1 1 │
#  └     ┘   └     ┘   └     ┘
#
```

TODO
----
- [ ] Support rendering transpose and inverse operations
- [ ] Allow wrapping of matrices and vectors in functions, e.g. `tanh`
- [ ] Highlight matching dimensions in the same colour
