from selenium.webdriver.common.by import By

from src.purchase_steps.steps_base import PurchaseStepBase
from src.driver import WebDriver


class AddtoCart(PurchaseStepBase):
    def __init__(
        self,
        driver: WebDriver,
        add_to_cart_text: str
    ) -> bool:
        self.driver = driver
        self._add_to_cart_text = add_to_cart_text

    @property
    def add_to_cart_text(self):
        return self._add_to_cart_text

    def run(self) -> bool:
        try:
            element = self.driver.find_element(By.XPATH, self.add_to_cart_text)
            element.click()
        except Exception as e: #TODO add actual exception
            print('Add to cart did not work.')
            print(e)
