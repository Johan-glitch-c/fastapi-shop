from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from ..database import get_db
from typing import Dict
from ..services.cart_sevices import CartService
from pydantic import BaseModel
from ..schemas.cart import CartResponseSchema, CartItemCreateSchema, CartItemUpdateSchema

router = APIRouter(
    prefix="/api/cart",
    tags=["cart"],
)

class AddToCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int,int] = {}

class UpdateCartRequest(BaseModel):
    product_id: int
    quantity: int
    cart: Dict[int,int] = {}

class RemoveCartRequest(BaseModel):
    cart: Dict[int,int] = {}

@router.post("/add", status_code=status.HTTP_200_OK)
def add_to_cart(request: AddToCartRequest,db: Session = Depends(get_db)):
    service=CartService(db)
    item=CartItemCreateSchema(product_id=request.product_id,quantity=request.quantity)
    updated_cart=service.add_to_cart(request.cart,item)
    return {"cart": updated_cart}



@router.get("",response_model=CartResponseSchema, status_code=status.HTTP_200_OK)
def get_cart(cart_data:Dict[int,int], db: Session = Depends(get_db)):
    service=CartService(db)
    return service.get_cart_details(cart_data)


@router.post("/update",status_code=status.HTTP_200_OK)
def update_cart_item(request: UpdateCartRequest, db: Session = Depends(get_db)):
    service=CartService(db)
    item=CartItemUpdateSchema(product_id=request.product_id,quantity=request.quantity)
    updated_cart=service.update_cart_item(request.cart,item)
    return {"cart": updated_cart}

@router.delete("/remove/{product_id}",status_code=status.HTTP_200_OK)
def remove_from_cart(product_id: int,request: RemoveCartRequest, db: Session = Depends(get_db)):
    service=CartService(db)
    updated_cart=service.remove_from_cart(request.cart, product_id)
    return {"cart": updated_cart}