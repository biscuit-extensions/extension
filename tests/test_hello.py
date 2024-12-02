from __future__ import annotations

import typing

from hello import setup

if typing.TYPE_CHECKING:
    from biscuit import App


class TestExtension:
    def test_init(self, app_instance: App):
        assert app_instance is not None

    def test_extension_setup(self, app_instance: App):
        setup(app_instance.api)
        assert True
