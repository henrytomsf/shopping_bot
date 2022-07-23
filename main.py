import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from src.product_url import ProductURL
from src.purchase_steps.add_to_cart import AddtoCart
from src.purchase_steps.check_availability import CheckAvailability
from src.product_id import ProductID
from src.purchase_steps.continue_shopping import ContinueShopping
from src.site_path import SitePath
from src.driver import WebDriver
from src.chrome_config import ChromeConfig
from src.chrome_driverpath import ChromeDriverPath



if __name__ == '__main__':
    wb = WebDriver(ChromeDriverPath.driver_path, ChromeConfig.chrome_options)
    # wb.driver.get('https://www.uniqlo.com/us/en/')
    # print(wb.driver.title)

    # define site and product id
    site_path = SitePath('https://www.uniqlo.com/us/en/products/')
    product_id = ProductID('E424873-000/00')

    #TODO implement pipeline to define steps

    # land on page with driver initially first
    wb.driver.get(ProductURL(site_path, product_id).url)

    # check if page available
    check_avail = CheckAvailability(site_path, product_id)
    if not check_avail.run():
        raise Exception('Page not available.')

    # ensure Add to cart element is found
    add_to_cart_element_text = '//button[text()="Add to cart"]'
    add_to_cart = AddtoCart(wb.driver, add_to_cart_element_text)
    add_to_cart.run()

    # wait for new window to load
    # hack
    time.sleep(10)

    # ensure Continue Shopping it clicked
    continue_shopping_element_text = '//button[text()="Continue shopping"]'
    continue_shopping = ContinueShopping(wb.driver, continue_shopping_element_text)
    continue_shopping.run()

    wb.driver.get('https://www.uniqlo.com/us/en/cart')
