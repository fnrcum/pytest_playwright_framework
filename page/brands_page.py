from playwright.sync_api import Page
from ..bases.common_settings import CommonSettings


class BrandsPage(CommonSettings):

    AVATAR_BUTTON = "#avatar-button"
    PROFILE_MODAL_ROLE = "input[data-testid='userProfileRole']"
    PROFILE_MODAL_FIRST_NAME = "input[data-testid='userProfileFirstName']"
    PROFILE_MODAL_LAST_NAME = "input[data-testid='userProfileLastName']"

    def __init__(self, page: Page):
        self.page = page

    def click_avatar_button(self) -> None:
        self.page.wait_for_selector(self.AVATAR_BUTTON).click()

    def navigate_to_page(self) -> None:
        self.page.goto(f"{self.BASE_URL}/brands")

    def get_profile_modal_role(self) -> str:
        return self.page.wait_for_selector(self.PROFILE_MODAL_ROLE).input_value()


