from fastapi import APIRouter, HTTPException
from schemas.holding import HoldingCreate, Holding
from services import holding_service

router = APIRouter(prefix="/holdings", tags=["Holdings"])

@router.post("")
def create_holding(holding: HoldingCreate):
    return holding_service.add_holding(holding)

@router.get("")
def get_holdings():
    return holding_service.list_all_holdings()

@router.delete("/{holding_id}", status_code=204)
def delete_holding(holding_id: int):
    deleted = holding_service.delete_holding(holding_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Holding not found")
    
@router.put("/{holding_id}")
def update_holding(holding_id: int, new_data: HoldingCreate):
    updated = holding_service.update_holding(holding_id, new_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Holding not found")
    return updated

