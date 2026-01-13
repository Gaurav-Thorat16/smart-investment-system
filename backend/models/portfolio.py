from pydantic import BaseModel

class Portfolio(BaseModel):
    risk_score: int
    risk_type: str
    equity_amount: float
    debt_amount: float
    gold_amount: float
    expected_return: float
