# -*- coding: utf-8 -*-
# Author:       Paulo Jacob
# Description:  The Either type is used to represent a value that can have two possible types
# Created at:   12-28-2023
from typing import Any, Callable


class Either:
    def match(self, on_error: Callable[[Exception], None], on_success: Callable[[Any], None]) -> None:
        if isinstance(self, Right):
            right: Right = self
            return on_success(right.result)

        if isinstance(self, Left):
            left: Left = self
            return on_error(left.error)

    def is_left(self) -> bool:
        return isinstance(self, Left)

    def get_result(self) -> Any | Exception:
        if isinstance(self, Right):
            right: Right = self
            return right.result

        if isinstance(self, Left):
            left: Left = self
            return left.error


class Right(Either):
    def __init__(self, result: Any):
        self.result = result


class Left(Either):
    def __init__(self, error: Exception):
        self.error = error
