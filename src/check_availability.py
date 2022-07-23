import requests

from src.http_codes import HTTPStatusCodes
from src.proxy_user_agent import ProxyUserAgent
from src.product_id import ProductID
from src.site_path import SitePath


class CheckAvailability:
    is_available = False

    def __init__(
        self,
        site_path: SitePath,
        product_id: ProductID
    ) -> None:
        self.site_path = site_path
        self.product_id = product_id
        self._product_url = self.site_path.path + self.product_id.id

    @property
    def product_url(self):
        return self._product_url

    def run(self) -> bool:
        headers = {'User-Agent': ProxyUserAgent.user_agent}
        resp = requests.get(self.product_url, headers=headers, timeout=2)

        if resp.status_code == HTTPStatusCodes.SUCCESS.value:
            CheckAvailability.is_available = True
            # insert logging to screen
            print('Page available.')

        return CheckAvailability.is_available
