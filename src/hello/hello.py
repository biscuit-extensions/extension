from __future__ import annotations

import typing

from biscuit.extensions import Extension

# Import any std/third-party lib here
# access any editor components from the `biscuit` module
# ...

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class Hello(Extension):
    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)

        # marks a simple log in biscuit logs tab
        self.api.logger.info(f"This is a sample log!")

        # for more control, you can access the biscuit instance (https://tomlin7.github.io/biscuit/api/app/)
        # app = self.api.base 

    def install(self) -> None:
        # optionally you can add any startup actions here
        self.api.notifications.info(f"Hello, Biscuit!")
