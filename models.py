from pydantic import BaseModel
from datetime import datetime


class Expense(BaseModel):
    name: str
    amount: float
    category: str
    created_on: datetime
