from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.component.header import Header
from dit.qa.pages.main_page.component.main import Main
from dit.qa.pages.main_page.component.sidebar import Sidebar

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(tag="nav")
    sidebar = Sidebar(class_name="sidebar")
    main = Main(id="content")
    footer = Component(tag="footer")
    loader = Component(id="loadingPage")

    @property
    def is_loader_hide(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.is_visible
                assert self.sidebar.is_visible
                assert self.main.is_visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()

    def wait_account_page(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.table.visible

                return self.main.title_account == ' ACCOUNTS'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Страница с созданием аккаунта не загружена')
        self.app.restore_implicitly_wait()

    def wait_lead_account(self) -> None:
        def condition() -> bool:
            try:
                assert self.main.view.visible
                assert self.main.list.visible
                assert self.is_loader_hide

                return self.main.title_account == 'NAMEACC'

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Страница Лида не загружена')
        self.app.restore_implicitly_wait()

    def wait_add_lead(self) -> None:
        def condition() -> bool:
            try:
                return self.main.name_lead.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Лид не был добавлен')
        self.app.restore_implicitly_wait()
