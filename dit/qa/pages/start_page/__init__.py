from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    title = Text(css='[class*="login_top"]')
    login = TextField(id="user_name")
    password = TextField(id="username_password")
    submit = Button(id="bigbutton")
    logo = Component(css='[class*="logo"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'SuiteCRM'
                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible

                return self.logo.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Стартовая страница не загружена')
        self.app.restore_implicitly_wait()
