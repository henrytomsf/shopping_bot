from selenium.webdriver.common.by import By

from src.purchase_steps.steps_base import PurchaseStepBase
from src.driver import WebDriver


class ContinueShopping(PurchaseStepBase):
    def __init__(
        self,
        driver: WebDriver,
        continue_shopping_text: str
    ) -> bool:
        self.driver = driver
        self._continue_shopping_text = continue_shopping_text

    @property
    def continue_shopping_text(self):
        return self._continue_shopping_text

    def run(self) -> bool:
        try:
            element = self.driver.find_element(By.XPATH, self.continue_shopping_text)
            element.click()
        except Exception as e: #TODO add actual exception
            print('Continue shopping did not work.')
            print(e)
