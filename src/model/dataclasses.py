from dataclasses import dataclass, asdict


@dataclass
class Book:
    title: str
    author: str
    year: int

    def get_dict(self):
        return asdict(self)
