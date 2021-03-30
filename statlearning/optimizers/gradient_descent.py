""" Simple gradient descent optimizer.

Sources:
    https://realpython.com/gradient-descent-algorithm-python/
"""

import logging
from typing import Callable

import attr
import numpy as np
import scipy.linalg


@attr.s(auto_attribs=True, repr=False, hash=False)
class GradientDescent(object):
    """ Class finding the minimum of a function given a function
    and gradient through gradient descent.

    Example use:
        Find the minimum of the function f(x) = x**2.

        gd = GradientDescent(gradient=lambda x: np.array([2 * x[0]])
    """
    gradient: Callable[[np.array], np.array]
    learning_rate: float = 0.1
    max_iters: int = 100
    tol: float = 1 * 10**-8

    def find_minimum(
        self,
        coordinate: np.array,
        n_iters: int = 0
    ) -> np.array:
        """ Find the minimum of the function using gradient descent.
        """
        learning_rate = self.learning_rate
        max_iters = self.max_iters
        gradient = self.gradient
        find_minimum = self.find_minimum
        tol = self.tol

        # End the search if the maximum number of iterations is reached.
        if n_iters >= max_iters:
            result = coordinate
            logging.debug(
                f"Returning result, {result} after {n_iters} calls"
            )

        # Otherwise, search for the minimum by traveling along the
        # negative gradient until the toleration is hit.
        else:
            step = -learning_rate * gradient(coordinate)

            new_coordinate = coordinate + step

            step_size = scipy.linalg.norm(step)

            within_tol = (step_size < tol)

            logging.debug(
                f"""
                Call {n_iters}: At {new_coordinate}, with step {step_size}.
                """
            )

            result = (
                new_coordinate if within_tol else
                find_minimum(
                    coordinate=new_coordinate,
                    n_iters=n_iters + 1
                )
            )

        return result
