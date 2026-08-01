from schemas.holding import HoldingCreate, Holding
from data.holdings import holdings

def list_all_holdings():
    return holdings

def add_holding(holding: HoldingCreate):
    new = Holding(id=len(holdings) + 1, **holding.model_dump())
    holding.append(new)
    return new

