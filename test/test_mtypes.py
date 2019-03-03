import functools

import pytest

from ndtypes import ndt
from xnd import xnd

from mtypes import mtype


def chain_marks(*marks):
    def inner(func):
        for mark in reversed(marks):
            func = mark(func)

        return func

    return inner


mark_input_types = pytest.mark.parametrize('input_type', [
    'int32', 'int64', 'uint32'
])

mark_output_types = pytest.mark.parametrize('output_type', [
    'int32', 'int64', 'uint32'
])

mark_both_types = chain_marks(mark_input_types, mark_output_types)


@mark_both_types
def test_mtypes(input_type, output_type):
    expected = ndt(input_type) == ndt(output_type)

    x = xnd(0, type=output_type)

    assert expected == isinstance(x, mtype[input_type])


@mark_both_types
def test_subclass(input_type, output_type):
    expected = ndt(input_type) == ndt(output_type)

    assert expected == issubclass(
        mtype[input_type], mtype[output_type])


@mark_input_types
def test_subclass_from_generic(input_type):
    assert issubclass(mtype[input_type], mtype)

@mark_input_types
def test_creation(input_type):
    x = mtype[input_type](0)

    assert isinstance(x, mtype[input_type])
