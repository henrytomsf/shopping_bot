from abc import ABC, abstractmethod


class PurchaseStepBase(ABC):
    @abstractmethod
    def run():
        ...
