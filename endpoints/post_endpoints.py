from ..helpers.api_helper import SessionWithUrlBase


class PostEndpoints:

    ALL_POSTS = "posts"

    def __init__(self):
        self.base = "https://jsonplaceholder.typicode.com/"
        self.session = SessionWithUrlBase(url_base=self.base)
        self.session.verify = False  # Just used for testing to ignore ssl errors

    def get_posts(self):
        return self.session.get(f"{self.ALL_POSTS}").json()

