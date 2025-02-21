from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Project:
    id: int
    name: str
    description: str
    technologies: List[str]
    start_date: date
    end_date: date