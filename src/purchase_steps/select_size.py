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
            self.driver.find_element_by_id(self.size).click()
            return True
        except Exception as e: #TODO add actual exception
            print('Click did not work.')
            print(e)
