from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    notification = Component(css='[class="desktop-bar"] [id="desktop_notifications"]')
    menu = Text(class_name='desktop-toolbar')
    profile = Component(css='[class="desktop-bar"] [id="globalLinks"]')
    create = Component(css='[class="desktop-bar"] [id="quickcreatetop"] ')
    logo = Button(css='[class*="home"]')
    marketing = Button(xpath='//a[text()="Marketing"]')
    account = Button(css='[id*="Accounts"]')

    @property
    def is_visible(self) -> bool:
        assert self.logo.visible
        assert self.menu == '  SALES  \n  MARKETING  \n  SUPPORT  \n  ACTIVITIES  \n  COLLABORATION  \n  ALL  '
        assert self.notification.visible
        assert self.profile.visible

        return self.create.visible


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
