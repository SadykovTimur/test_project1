from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField

__all__ = ['Main']


class MainWrapper(ComponentWrapper):
    title = Text(css='[class*="nav-dashboard"]')
    container = Component(id="pageContainer")
    title_account = Text(tag="h2")
    table = Component(css='[class*="table-responsive"]')
    panel = Component(class_name='panel-content')
    view = Component(class_name='detail-view')
    agent = Button(xpath="//a[contains(text(),'AutotestAgent123')]")
    create = Button(css='[class*="action_button"] span')
    leads_title = Button(id="subpanel_title_leads")
    account_lead = Button(id="account_leads_select_button")
    checkbox = Button(xpath='(//a[text()="Autotest123"]/preceding::input[@class="checkbox"])[3]')
    name_lead = Component(xpath='//a[text()="Autotest123"]')
    last_name = TextField(id="last_name")
    name = TextField(id="name")
    save = Button(id="SAVE")
    list_view = Button(id="listViewNextButton_bottom")

    @property
    def is_visible(self) -> bool:
        assert self.title == 'SUITECRM DASHBOARD\nACTIONS'

        return self.container.visible


class Main(Component):
    def __get__(self, instance, owner) -> MainWrapper:
        return MainWrapper(instance.app, self.find(instance), self._locator)
