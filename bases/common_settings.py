import os


class CommonSettings:

    BASE_URL = f"https://{os.getenv('ENVIRONMENT')}.<url>.com/"
