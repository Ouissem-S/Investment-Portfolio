from schemas.holding import HoldingCreate, Holding
from data.holdings import holdings

def list_all_holdings():
    return holdings

def add_holding(holding: HoldingCreate):
    new = Holding(id=len(holdings) + 1, **holding.model_dump())
    holdings.append(new)
    return new

def delete_holding(holding_id: int):
    for holding in holdings:
        if holding.id == holding_id:
            holdings.remove(holding)
            return True
    return False
    
def update_holding(holding_id: int, new_data: HoldingCreate):
    for i, holding in enumerate(holdings):
        if holding.id == holding_id:
            holdings[i] = Holding(id=holding_id, **new_data.model_dump())
            return holdings[i]
    return None
