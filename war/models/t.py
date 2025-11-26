from typing import Dict, List
from dataclasses import dataclass
import streamlit as st
"""
from dataclasses import dataclass

@dataclass
class Fruit:
    fruit_type:str
    price:int

# instantition period(object creation period)
vitamin = Fruit(fruit_type="orange", price=10)

# accessing the attributes of the class
print(vitamin.fruit_type, vitamin.price)


MONTHLY_FEES:Dict[int, float]={
    1:25.0,
    2:30.00,
    3:35.00
}

print(MONTHLY_FEES[1])


id_number=987
profile="image"
name="moses"
martial_arts="martial"
current_weight=97.6
category="category"
competition_per_month=9
private_coaching_hours=4

@dataclass
class Athlete:
    id_number:int
    profile_image:str
    name:str
    martial_arts:str
    current_weight:float
    category:str
    competition_per_month:int
    private_coaching_hours: int  # max 5

    def base_fee(self)->float:
        total_martial_arts_studies = MONTHLY_FEES.get(len(self.martial_arts))
        return MONTHLY_FEES[total_martial_arts_studies]


ath=Athlete(id_number, profile, name, martial_arts, current_weight, category, competition_per_month, private_coaching_hours)

print(ath.current_weight)

def access(athlete):
    print(base_fee)
"""
user = 1
martial_arts=["joj", "jdddf", "adwd"]

MONTHLY_FEES:Dict[int, float]={
    1:25.0,
    2:30.00,
    3:35.00
}


def base_fee()->float:
    return MONTHLY_FEES.get(len(martial_arts))

print(base_fee())
       



























