from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    title = Text(css='[class*="nav-dashboard"]')
    container = Component(id="pageContainer")
    title_account = Text(tag="h2")
    table = Component(css='[class*="table-responsive"]')
    view = Component(class_name='detail-view')
    list = Component(id="subpanel_list")
    lead = Button(xpath="//a[contains(text(),'NameAcc')]")
    create = Button(css='[class*="action_button"] span')
    leads_title = Button(id="subpanel_title_leads")
    account_lead = Button(id="account_leads_select_button")
    checkbox = Components(css='[class="checkbox"]')
    select = Button(id="MassUpdate_select_button")
    name_lead = Component(xpath='//a[text()="Name Surname"]')

    @property
    def is_visible(self) -> bool:
        assert self.title == 'SUITECRM DASHBOARD\nACTIONS'

        return self.container.visible


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
