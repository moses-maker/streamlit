from dataclasses import dataclass

@dataclass  # this makes the fields immutable i.e unchangeable
class Units:
    currency: str = "Ksh"
    weight: str = "Kg"
    time: str = "Hrs"

    
