import os


class CommonSettings:

    BASE_URL = f"https://{os.getenv('ENVIRONMENT')}.<env>.com/"
