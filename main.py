from typing import List

import requests
from selenium.webdriver.common.keys import Keys

from src.driver import WebDriver
from src.chrome_config import ChromeConfig
from src.chrome_driverpath import ChromeDriverPath



if __name__ == '__main__':
    wb = WebDriver(ChromeDriverPath.driver_path, ChromeConfig.chrome_options)
    wb.driver.get('https://www.uniqlo.com/us/en/')
    print(wb.driver.title)
