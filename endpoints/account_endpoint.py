from ..helpers.api_helper import SessionWithUrlBase


class AccountEndpoint:

    ACCOUNT = "Account"

    def __init__(self, base: str):
        self.session = SessionWithUrlBase(url_base=base)
        self.session.headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        self.session.verify = True  # Just used for testing to ignore ssl errors

    def login(self, username: str, password: str):
        data = self.session.post(f"{self.ACCOUNT}", data={"username": username, "password": password})
        return data