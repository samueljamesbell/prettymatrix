prettymatrix
============

[![Build Status](https://travis-ci.org/samueljamesbell/prettymatrix.svg?branch=master)](https://travis-ci.org/samueljamesbell/prettymatrix)

Struggling to tell your rows from your columns?

`prettymatrix` pretty prints your matrices and vectors, just like you're used
to.

Installation
------------
Available through pip:

```
pip install prettymatrix
```

Examples
--------
```
import prettymatrix

M = np.array([['1', '22'], ['333', '4444']])

print(prettymatrix.matrix_to_string(M))

# =>
#  ┌          ┐
#  │ 1   22   │
#  │ 333 4444 │
#  └          ┘
#
```

Annotate your matrix with a name:

```
import prettymatrix

M = np.array([['0'], ['0']])

print(prettymatrix.matrix_to_string(M, name='M_x_y'))

# =>
#  ┌   ┐
#  │ 0 │
#  │ 0 │
#  └   ┘
#  M_x_y
#
```

Or its dimensions:

```
import prettymatrix

M = np.array([['0'], ['0']])

print(prettymatrix.matrix_to_string(M, include_dimensions=True))

# =>
#  ┌   ┐
#  │ 0 │
#  │ 0 │
#  └   ┘
#  (2x1)
#
```
