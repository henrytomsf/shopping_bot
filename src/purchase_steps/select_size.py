from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from src.purchase_steps.steps_base import PurchaseStepBase
from src.driver import WebDriver


class SelectSize(PurchaseStepBase):
    def __init__(
        self,
        driver: WebDriver,
        size: str
    ) -> None:
        self.size = size
        self.driver = driver

    def run(self) -> bool:
        try:
            element = self.driver.find_element(By.XPATH, "//*[@id='{}']".format(self.size))
            ActionChains(self.driver).move_to_element(element).perform()
            ActionChains(self.driver).click(element).perform()
            return True

        except Exception as e: #TODO add actual exception
            print('Click did not work.')
            print(e)
