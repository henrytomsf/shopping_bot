from selenium import webdriver

from src.chrome_config import ChromeConfig
from src.chrome_driverpath import ChromeDriverPath


class WebDriver:
    def __init__(
        self,
        driver_path: ChromeDriverPath,
        chrome_config: ChromeConfig
    ) -> None:
        self.driver_path = driver_path
        self.chrome_config = chrome_config
        self.driver = webdriver.Chrome(driver_path, chrome_options=self.chrome_config)
