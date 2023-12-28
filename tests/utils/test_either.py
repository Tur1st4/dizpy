# -*- coding: utf-8 -*-
# Author:       Paulo Jacob
# Description:  Test Either class
# Created at:   12-28-2023
from src.utils.either import Right, Left, Either


def return_right() -> Either:
    return Right(True)


def return_left() -> Either:
    return Left(Exception("Generic error"))


def test_either():
    res_r: Either = return_right()
    res_l: Either = return_left()

    assert isinstance(res_r, Right)
    assert isinstance(res_l, Left)
    assert res_r.is_left() is False
    assert res_l.is_left() is True
    assert type(res_r.get_result()) is bool
    assert type(res_l.get_result()) is Exception
