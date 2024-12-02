from __future__ import annotations

import typing

from .hello import Hello

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: ExtensionsAPI) -> None:
    api.register("hello", Hello(api))
