from __future__ import annotations

import typing

from .extension import ExtensionClass

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


def setup(api: "ExtensionsAPI") -> None:  # noqa: D401
    """Entrypoint for Biscuit to load the extension."""
    api.register("{{cookiecutter.extension_name}}", ExtensionClass(api)) 