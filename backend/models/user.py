from pydantic import BaseModel

class UserProfile(BaseModel):
    age: int
    monthly_income: float
    investment_amount: float
    investment_years: int
    risk_appetite: str
