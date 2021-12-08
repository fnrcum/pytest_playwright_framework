import pytest
from playwright.sync_api import Page
from ..page.login_page import LoginPage
from ..data.users import Users
from ..bases.common_settings import CommonSettings


class TestLogin(CommonSettings):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)

    @pytest.mark.parametrize('email, password', [
        (Users.ADMINISTRATOR["username"], Users.ADMINISTRATOR["password"]),
    ])
    @pytest.mark.login
    def test_login(self, email, password):
        """
        Login page very long description here for user
        """
        self.login_page.navigate_to_page()
        self.login_page.click_login_redirect_button()
        self.login_page.okta_login(email, password)
        # self.brands_page.click_avatar_button()
        # role = self.brands_page.get_profile_modal_role()
        # assert role.lower() in email.lower()
