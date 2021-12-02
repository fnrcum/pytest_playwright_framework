import pytest
from playwright.sync_api import Page
from ..page.playground_page import PlaygroundPage


class Tests:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page
        self.playground_page = PlaygroundPage(page)

    @pytest.mark.parametrize('value_A,value_B', [
        # each element of this list will provide values for the
        # topics "value_A" and "value_B" of the test and will
        # generate a stand-alone test case.
        ('first case', 1),
        ('second case', 2),
    ])
    @pytest.mark.param
    def test_func(self, page, value_A, value_B):
        """Test Showing us how params work in PyTest"""
        self.page.goto("http://www.uitestingplayground.com/")
        self.page.click("text=Click")
        self.page.click("#badButton")
        assert value_A in ["first case", "second case"]
        assert value_B in [1, 2]

    @pytest.mark.click
    def test_click(self):
        self.page.goto("http://www.uitestingplayground.com/")
        self.page.click("text=Click")
        import logging
        logging.warning(f"Printing this:   {self.playground_page.bad_button}")
        self.playground_page.bad_button.click()

    @pytest.mark.loadDelay
    def test_load_delay(self, page):
        self.page.goto("http://www.uitestingplayground.com/")
        self.page.click("text=Load Delay")
        self.page.click(".btn")

    @pytest.mark.input
    def test_input(self, page):
        """Test showing us how input works. Intentional fail"""
        self.page.goto("http://www.uitestingplayground.com/textinput")
        self.page.fill("#newButtonName", "Some New Name")
        self.page.click("#updatingButton")
        assert page.inner_text("#updatingButton") == "Some New Name1", "Intentional fail"

    @pytest.mark.fail
    def test_scrollbars(self, page):
        """Failing test on purpose"""
        self.page.goto("http://www.uitestingplayground.com/scrollbars")
        self.page.click("#hidingButton")
        assert 1 == 2, "Intentional fail"

    def test_login_fail(self, page):
        self.page.goto("http://www.uitestingplayground.com/sampleapp")
        self.page.fill('//input[@placeholder="User Name"]', "Nicu")
        self.page.click("#login")
        assert page.inner_text("#loginstatus") == "Invalid username/password"

    def test_login_logout(self, page):
        self.page.goto("http://www.uitestingplayground.com/sampleapp")
        self.page.fill('//input[@placeholder="User Name"]', "Nicu")
        self.page.fill('//input[@name="Password"]', "pwd")
        self.page.click("#login")
        assert page.inner_text("#loginstatus") == "Welcome, Nicu!"

        # logout
        self.page.click("#login")
        assert self.page.inner_text("#loginstatus") == "User logged out."

    def test_nonbreakingspace(self, page):
        self.page.goto("http://www.uitestingplayground.com/nbsp")
        self.page.click("text=My Button")

    def test_progress_bar(self, page):
        self.page.goto("http://www.uitestingplayground.com/progressbar")
        self.page.click("#startButton")
        self.page.inner_text("#progressBar[aria-valuenow='75']")
        self.page.click("#stopButton")
        assert "Result: 0" in self.page.inner_text("#result")
