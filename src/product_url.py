from dataclasses import dataclass

from src.product_id import ProductID
from src.site_path import SitePath


@dataclass
class ProductURL:
    path: SitePath
    product_id: ProductID

    @property
    def url(self):
        return self.path.path + self.product_id.id
