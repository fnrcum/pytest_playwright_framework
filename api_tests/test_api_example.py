import pytest
from ..endpoints.post_endpoints import PostEndpoints
from ..bases.common_settings import CommonSettings


class TestsPosts(CommonSettings):
    """
    API used for the example https://jsonplaceholder.typicode.com/
    """
    @pytest.fixture(autouse=True)
    def setup(self):
        self.post_endpoints = PostEndpoints()

    @pytest.mark.api
    def test_api_posts(self):
        """Some very long name or description"""
        data = self.post_endpoints.get_posts()
        assert len(data) > 0, "Test data too long"
