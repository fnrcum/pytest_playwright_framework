from playwright.sync_api import Page


class PlaygroundPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def bad_button(self):
        return self.page.wait_for_selector("#badButton")