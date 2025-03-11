from __future__ import annotations

import typing

from .hello import Hello

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: ExtensionsAPI) -> None:
    """Defines the entrypoint to the extension.

    NOTE: `setup(api)` must be present in `src/extension_name/__init__.py`

    Normally, `api.register(id, instance)` is called within `setup`
    if you are expecting it to communicate with other loaded extensions."""

    api.register("hello", Hello(api))

