from typing import Optional
from pydantic import BaseModel, Field


class CartItemsBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be greater than 0)")


class CartItemCreateSchema(CartItemsBase):
    pass


class CartItemUpdateSchema(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New quantity (must be greater than 0)")


class CartItemSchema(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Subtotal in cart")
    image_url: Optional[str] = Field(None, description="Image url")


class CartResponseSchema(BaseModel):
    items: list[CartItemSchema] = Field(..., description="list of cart items")
    total: float = Field(..., description="Total price in cart")
    items_count: int = Field(..., description="Number of items in cart")