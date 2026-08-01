from fastapi import APIRouter
from schemas.holding import HoldingCreate, Holding
from services import holding_service

router = APIRouter(prefix="/holdings", tags=["Holdings"])

@router.post("")
def create_holding(holding: HoldingCreate):
    return holding_service.add_holding(holding)

@router.get("")
def get_holdings():
    return holding_service.list_all_holdings()
