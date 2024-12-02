from __future__ import annotations

import typing

import pytest
from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class Hello(Extension):
    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)

        self.api.logger.info(f"This is a sample log!")

    def install(self) -> None:
        self.api.notifications.info(f"Hello, Biscuit!")
