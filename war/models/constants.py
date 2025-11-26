from typing import Dict

# monthly training fee based on arts studied.
MONTHLY_FEES:Dict[int, float]={
    1:25.0,
    2:30.00,
    3:35.00
}

# weight category upper limit
WEIGHT_LIMITS:Dict[str, float]={
    "Half LightwWight":66.0,
    "LightWeight":73.0,
    "Half MiddleWeight":81.0,
    "MiddleWeight":90.0,
    "Half HeavyWeight":100.0,
    "HeavyWeight":float("inf")
}

# private coaching houly rate
PRIVATE_RATE = 9.50

