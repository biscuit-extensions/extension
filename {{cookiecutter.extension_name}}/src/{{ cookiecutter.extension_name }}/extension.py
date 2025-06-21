from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class ExtensionClass(Extension):
    """A simple Biscuit extension that shows a greeting notification."""

    def __init__(self, api: "ExtensionsAPI") -> None:  # noqa: D401
        super().__init__(api)
        self.api.logger.info("{{cookiecutter.extension_name}} extension initialised.")

    def install(self) -> None:  # noqa: D401
        """Run after the extension is loaded."""
        self.api.notifications.info("Hello, Biscuit!") 