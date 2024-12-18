import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'create_lead',
    'create_agent',
    'check_connection',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def create_lead(app: Application, last_name: str = "Autotest123") -> None:
    with allure.step('Creating lead'):
        try:
            page = MainPage(app)
            page.header.marketing.click()
            page.header.leads.click()

            page.wait_leads()

            page.sidebar.create_lead.click()
            page.wait_create()
            page.main.last_name.send_keys(last_name)
            page.main.save.click()
            page.wait_create_leads()

            screenshot_attach(app, 'create_lead')
        except Exception as e:
            screenshot_attach(app, 'create_lead_error')

            raise e


def create_agent(app: Application, name: str = "AutotestAgent123") -> None:
    with allure.step('Creating agent'):
        try:
            page = MainPage(app)
            page.header.marketing.click()
            page.header.account.click()

            page.wait_accounts()

            page.sidebar.create_lead.click()
            page.wait_create()
            page.main.name.send_keys(name)
            page.main.save.click()

            page.wait_create_agent()

            screenshot_attach(app, 'create_agent')
        except Exception as e:
            screenshot_attach(app, 'create_agent_error')

            raise e


def check_connection(app: Application) -> None:
    with allure.step('Checking connection'):
        try:
            page = MainPage(app)
            page.header.marketing.click()
            page.header.account.click()

            page.wait_accounts()

            page.main.list_view.click()
            page.main.list_view.click()

            page.main.agent.click()
            page.wait_create_agent()

            page.main.leads_title.click()
            page.main.create.click()
            page.main.account_lead.click()
            app.driver.switch_to.window(app.driver.window_handles[1])
            page.button_last.click()
            page.main.checkbox[0].webelement.click()
            page.select.click()

            page.wait_add_lead()

            screenshot_attach(app, 'check_connection')
        except Exception as e:
            screenshot_attach(app, 'check_connection_error')

            raise e
