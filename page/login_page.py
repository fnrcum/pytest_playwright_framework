from playwright.sync_api import Page
from ..bases.common_settings import CommonSettings


class LoginPage(CommonSettings):

    LOGIN_BUTTON = ".LoginFormView_login__2bSoV a"
    OKTA_USERNAME_FIELD = "#okta-signin-username"
    OKTA_PASSWORD_FIELD = "#okta-signin-password"
    OKTA_SIGNIN_BUTTON = "#okta-signin-submit"

    def __init__(self, page: Page):
        self.page = page

    def click_login_redirect_button(self) -> None:
        self.page.wait_for_selector(self.LOGIN_BUTTON).click()

    def navigate_to_page(self) -> None:
        self.page.goto(self.BASE_URL)

    def okta_login(self, user: str, password: str) -> None:
        self.page.wait_for_selector(self.OKTA_USERNAME_FIELD).fill(user)
        self.page.wait_for_selector(self.OKTA_PASSWORD_FIELD).fill(password)
        self.page.wait_for_selector(self.OKTA_SIGNIN_BUTTON).click()


