class Employee:
    """
        name: str
        id: int
        birth_date: datetime #import datetime
        Position: str
        Benefits: list => ["insurance", "social security"]
    """
    pass
"""
calculate_income

"""

class PartTimer(Employee):
    """
        hourly_rate: float
        worked_hours: float
    """
    pass

class FullTimer(Employee):
    """
        salary
        overtime_hours => hours * (salary/4/5/8) * 1.5
    """
    pass