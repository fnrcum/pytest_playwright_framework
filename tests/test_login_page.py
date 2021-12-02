import pytest
from playwright.sync_api import Page
from ..page.login_page import LoginPage
from ..page.brands_page import BrandsPage
from ..data.users import Users
from ..bases.common_settings import CommonSettings


class TestLogin(CommonSettings):

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)
        self.brands_page = BrandsPage(page)

    @pytest.mark.parametrize('email, password', [
        (Users.ADMINISTRATOR["username"], Users.ADMINISTRATOR["password"]),
        (Users.ACCOUNT_MANAGER["username"], Users.ACCOUNT_MANAGER["password"]),
        (Users.MARKETEER["username"], Users.MARKETEER["password"]),
        (Users.MERCHANDISER["username"], Users.MERCHANDISER["password"]),
        (Users.PLANNER["username"], Users.PLANNER["password"]),
        (Users.READ_ONLY["username"], Users.READ_ONLY["password"]),
        (Users.CUSTOMER["username"], Users.CUSTOMER["password"])
    ])
    @pytest.mark.login
    def test_login(self, email, password):
        """
        Login page very long description here for user
        """
        self.login_page.navigate_to_page()
        self.login_page.click_login_redirect_button()
        self.login_page.okta_login(email, password)
        self.brands_page.click_avatar_button()
        role = self.brands_page.get_profile_modal_role()
        assert role.lower() in email.lower()
