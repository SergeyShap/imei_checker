from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_bot_token: str
    telegram_whitelist: str
    api_auth_tokens: str
    imei_check_api_token: str

    class Config:
        env_file = ".env"

    @property
    def telegram_whitelist_as_list(self) -> List[int]:
        """Преобразует строку TELEGRAM_WHITELIST в список целых чисел."""
        return [int(item.strip()) for item in self.telegram_whitelist.split(",")]

    @property
    def api_auth_tokens_as_list(self) -> List[str]:
        """Преобразует строку API_AUTH_TOKENS в список строк."""
        return [item.strip() for item in self.api_auth_tokens.split(",")]

# Загрузка настроек
settings = Settings()

# Вывод настроек для проверки
print("Telegram Bot Token:", settings.telegram_bot_token)
print("Telegram Whitelist:", settings.telegram_whitelist_as_list)
print("API Auth Tokens:", settings.api_auth_tokens_as_list)
print("IMEI Check API Token:", settings.imei_check_api_token)