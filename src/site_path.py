from dataclasses import dataclass


@dataclass
class SitePath:
    path: str

    def __post_init__(self):
        if not self.path.endswith('/'):
            raise ValueError(f'{self.path} needs to end with /')
