import unittest
import numpy as np
import numpy.testing as npt

from ols_example import linalg

################################################################################

class LinalgTestCase(unittest.TestCase):
    """Class for linear algebra tests."""

    ############################################################################

    def test_check_elements(self):
        """check_elements"""

        empty_array = np.empty(10)
        full_array = np.ones(10)

        assert linalg.check_elements(empty_array), "Test input empty array."
        assert linalg.check_elements(full_array), "Test input full array."

    ############################################################################

    def test_check_2d(self):
        """check_2d"""

        with self.assertRaises(Exception) as context:
            linalg.check_2d(1.0)
        self.assertTrue('Input must be an ndarray.' in str(context.exception))

        one_d = np.ones((10,))
        output = linalg.check_2d(one_d)

        one_d = np.ones((10,1))
        output = linalg.check_2d(one_d)

        one_d = np.ones((10,1,1))
        output = linalg.check_2d(one_d)

        two_d = np.ones((10,10))
        output = linalg.check_2d(two_d)

        two_d = np.ones((10,10,1))
        output = linalg.check_2d(two_d)

    ############################################################################

    def test_identity_matrix(self):
        """identity_matrix"""

        true_identity = np.asarray([[1,0,0],[0,1,0],[0,0,1]])

        identity = linalg.identity_matrix(3)

        npt.assert_equal(true_identity, identity)

    ############################################################################

    def test_copy_matrix(self):
        """copy_matrix"""

        input_arr = np.random.normal(0, 3, (10, 4))

        copy_arr = linalg.copy_matrix(input_arr)

        npt.assert_equal(input_arr, copy_arr)

    ############################################################################

    def test_is_invertible(self):
        """is_invertible"""

        A = np.random.normal(0, 10, (10, 10))

        assert linalg.is_invertible(A), "Flagged inveretible matrix as non-invertible."

    ############################################################################

    def test_transpose(self):
        """transpose"""

        input_arr = np.random.normal(0, 3, (10, 4))

        true_transposed = input_arr.T

        transposed = linalg.transpose(input_arr)

        npt.assert_equal(true_transposed, transposed)

    ############################################################################

    def test_matmul(self):
        """matmul"""

        A = np.random.normal(0, 3, (10, 2))
        B = np.random.normal(0, 3, (2, 10))

        True_C = A.dot(B)

        C = linalg.matmul(A, B)

        npt.assert_almost_equal(True_C, C)

    ############################################################################

    def test_invert_matrix(self):
        """invert_matrix"""

        A = np.random.normal(0, 10, (10, 10))
        true_invert = np.linalg.inv(A)

        invert = linalg.invert_matrix(A)

        npt.assert_almost_equal(true_invert, invert)

if __name__ == '__main__':
    unittest.main(failfast=True)
