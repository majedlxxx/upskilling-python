from datetime import datetime
from typing import List, Tuple
from department import Department


class Employee:
    """
        name: str
        id: int
        birth_date: datetime #import datetime
        position: str
        benefits: list => ["insurance", "social security"]
    """
    def __init__(self, name: str, id: int, birth_date: datetime, position: str, benefits: List[str], department: Department) -> None:
        self.name = name
        self.birth_date = birth_date
        self.position = position
        self.benefits = benefits
        self.department = department



class PartTimer(Employee):
    """
        Salary: hourly_rate * working_hours
    """
    def __init__(self, name: str, id: int, birth_date: datetime, position: str, benefits: List[str], department: Department, hourly_rate: float = 0) -> None:
        super().__init__(name, id, birth_date, position, benefits, department)
        self.hourly_rate = hourly_rate
        self.working_hours = 0
    
    def calculate_income(self) -> float:
        return self.hourly_rate * self.working_hours

class FullTimer(Employee):
    """
        salary
        overtime_hours => hours * (salary/4/5/8) * 1.5
    """
    def __init__(self, name: str, id: int, birth_date: datetime, position: str, benefits: List[str], department: Department, salary: float = 0) -> None:
        super().__init__(name, id, birth_date, position, benefits)
        self.salary = salary
        self.overtime_hours = 0
        
    def calculate_income(self) -> float:
        hourly_rate = self.salary / 4 / 5 / 8 # 4 weeks/ 5 working days / 8 working hours
        return self.salary + self.overtime_hours * hourly_rate
    
    def apply_raise(self, percentage: float) -> None:
        """
            percentage => 1% upto 100% 
            example:
            salary: 1000
            percentage: 20
            new_salary: 1200
            Update salary
        """
        self.salary = (1 + percentage/100)  * self.salary
        
    def get_bonus(self, percentage: float) -> float:
        """
            percentage of the yearly salary
            eg: 
            salary: 1000
            percentage: 10
            bonus: 1000*12 * 10% = 1200
        """
        return self.salary * 12 * (20/100)
        




