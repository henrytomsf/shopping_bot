from typing import List

from src.product_url import ProductURL
from src.check_availability import CheckAvailability
from src.product_id import ProductID
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

    # land on page with driver initially first
    wb.driver.get(ProductURL(site_path, product_id).url)

    # check if page available
    check_avail = CheckAvailability(site_path, product_id)
    for i in range(2): #TODO abstract this check
        if check_avail.run():
            break

    # select size
    wb.driver.find_element_by_id('M').click()
    