"""
A from scratch implementation of the linear algebra operations required for
ordinary least squares regression. I try to avoid built in numpy functions with
the exception of the ndarray data type. The code here could easily be recreated
without numpy using lists instead of numpy arrays.
"""

import sys
import numpy as np

################################################################################

def check_elements(arr):
    """Check that the array is not empty."""
    return arr.ndim and arr.size

def check_2d(a, left_orient=True):
    """
    Make sure that the input is a 2D matrix.
    """

    # check that instance type is ndarray
    assert isinstance(a, np.ndarray), "Input must be an ndarray."

    # squeeze extra dimensions and convert to floats
    a = a.squeeze().astype(np.float64)

    # throw error if the matrix is empty
    if check_elements(a) == 0:
        raise Exception("Matrix is empty.")

    # reshape scalars to matricies
    if a.ndim == 0 and a.size == 1:
        if left_orient:
            return a.reshape(-1, 1)
        else:
            return a.reshape(1, -1)

    # reshape vectors to matricies
    if len(a.shape) == 1:
        if not left_orient:
            return a.reshape(-1, 1)
        else:
            return a.reshape(1, -1)

    # throw error if a tensor is input
    if len(a.shape) > 2:
        raise Exception("Matrix has too many dimensions.")

    return a

def identity_matrix(n):
    """
    Creates and returns an identity matrix.
    """
    # initialize a 2D matrix with zeros
    I = np.zeros((n, n))

    # fill the diagonal with ones
    for i in range(n):
        I[i][i] = 1.0

    return I

def copy_matrix(M):
    """
    Output a copy of the input matrix.
    """

    rows = M.shape[0]
    cols = M.shape[1]

    MC = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
    return MC

def is_invertible(arr, strength='condition'):
    """
    Function to return True is matrix is safely invertible and
    False is the matrix is not safely invertable.
    """
    if strength == 'cramer':
        return np.linalg.det(arr) == 0.0
    if strength == 'rank':
        return arr.shape[0] == arr.shape[1] and np.linalg.matrix_rank(arr) == arr.shape[0]
    return 1.0 / np.linalg.cond(arr) >= sys.float_info.epsilon

################################################################################

def transpose(m):
    """
    Transpose a 2D matrix.
    """

    # get the dimensions of the matrix
    rows = m.shape[0]
    cols = m.shape[1]

    # create an emtpy array
    output = np.zeros((cols, rows))

    # flip the rows and columns of m and insert into ouput
    for j in range(cols):
        for i in range(rows):
            output[j][i] = m[i][j]
    return output

    # a single line implementation
    #return np.asarray([[m[j][i] for j in range(rows)] for i in range(cols)])

def matmul(a, b):
    """
    """

    # ensure matricies are 2D
    a = check_2d(a)
    b = check_2d(b, False)

    ar, ac = a.shape # n_rows, n_cols
    br, bc = b.shape # n_rows, n_cols

    # Check that inner dimensions match, rows == columns
    assert ac == br, "Inner dimensions do not match: {}, {}".format(ac, br)

    c = np.zeros((ar, bc))
    for i in range(ar):
        for j in range(bc):
            for k in range(ac): # ac == br, so could use br
                c[i, j] += a[i,k] * b[k,j]

    return c

def invert_matrix(A, tol=None):
    """
    Find the inverse of a 2D square matrix.

    A' is the inverse of A

    AX = IB
    IX = A'B

    Am -> I
    Im -> A'
    """

    # ensure matrix is 2D
    A = check_2d(A)
    # ensure the matrix is square
    assert A.shape[0] == A.shape[1], "A is not a square matrix."
    # check if matrix is singular
    assert is_invertible(A)

    n = A.shape[0] # number of rows for A
    AM = copy_matrix(A) # copy the matrix A
    I = identity_matrix(n) # get an identity matrix matching dimensions in A
    IM = identity_matrix(n) # get an identity matrix matching dimensions in A

    indices = [i for i in range(n)] # for flexible row referencing

    for fd in range(n): # fd = focus diagonal
        fdScaler = 1.0 / AM[fd][fd]

        # vectorized
        AM[fd] = AM[fd] * fdScaler
        IM[fd] = IM[fd] * fdScaler

        # not vectorized
        # for j in range(n): # loop over columns
        #     AM[fd][j] *= fdScaler
        #     IM[fd][j] *= fdScaler

        for i in indices[0:fd] + indices[fd+1:]: # loop over all rows except fd

            crScaler = AM[i][fd] # cr stands for "current row".

            # vectorized
            AM[i] = AM[i] - crScaler * AM[fd]
            IM[i] = IM[i] - crScaler * IM[fd]

            # not vectorized
            # for j in range(n):
            #     AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            #     IM[i][j] = IM[i][j] - crScaler * IM[fd][j]

    return IM
