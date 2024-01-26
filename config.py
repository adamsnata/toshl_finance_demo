



from typing import Literal

import pydantic_settings

EnvContext = Literal['local_emulator', 'bstack', 'local_real']


class Config(pydantic_settings.BaseSettings):
    context: EnvContext = 'bstack'
    timeout: float = 10.0
    API_URL: str = 'https://toshl.com'
    TEST_USER_EMAIL: str = 'yulia.shilkova+toshl@gmail.com'
    TEST_USER_PASSWORD: str = 'test_password'
    TEST_USER_NAME: str = 'Iuliia Shilkova'

config = Config()
