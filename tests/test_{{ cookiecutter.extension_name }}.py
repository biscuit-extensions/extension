from __future__ import annotations

import sys
import typing

sys.path.append("..")

from src.{{cookiecutter.extension_name}} import setup

if typing.TYPE_CHECKING:
    from biscuit import App


class TestExtension:
    def test_extension_setup(self, app_instance: "App") -> None:  # noqa: D401
        """Ensure extension setup runs without raising errors."""
        setup(app_instance.api)
        assert True