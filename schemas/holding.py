from pydantic import BaseModel, Field

class HoldingCreate(BaseModel):
    symbol: str = Field(..., min_length=1, max_length=10)
    quantity: int = Field(..., gt=0)
    average_price: float = Field(...,gt=0)
    
class Holding(HoldingCreate):
    id: int
    
