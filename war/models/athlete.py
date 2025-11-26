from dataclasses import dataclass
from typing import List
from .constants import MONTHLY_FEES, PRIVATE_RATE, WEIGHT_LIMITS
from .units import Units

@dataclass
class Athlete:
    id_number:int
    profile:bytes
    name:str
    martial_arts:List[str]
    current_weight:float
    category:str
    competition_per_month:int
    private_coaching_hours: int  # max 5

    def base_fee(self)->float:
        return MONTHLY_FEES[self.martial_arts]
       

    def coaching_fee(self)->float:
        return min(self.private_coaching_hours, 5)*PRIVATE_RATE

    def total_fee(self)->float:
        return self.base_fee() + self.coaching_fee()

    def weight_status(self)->str:
        category_limit = WEIGHT_LIMITS.get(self.category, float("inf"))
        if self.current_weight <= category_limit:
            return f"Eligible for {self.category} (within {category_limit}{Units.weight} limit)"

        else:
            return f"Overweight for {self.category} (limit:{category_limit}{Units.weight})"