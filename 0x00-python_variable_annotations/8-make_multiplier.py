#!/usr/bin/env python3
"""Type-annotated function 'make_multiplier' which takes
a float multiplier as argument, returns a function which
multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns function which multiplies a float by multiplier"""
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
