from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponseSchema


class ProductBase(BaseModel):
    name: str = Field(...,min_length=5,max_length=200,
                      description="Product name")
    description: Optional[str]= Field(None,description="Product description")
    price: float = Field(...,gt=0,description="Product price (must be greater than 0)")
    category_id: int = Field(...,description="Product category id")
    image_url: Optional[str]= Field(None,description="Product image url")


class ProductCreateSchema(ProductBase):
    pass


class ProductResponseSchema(BaseModel):
    id: int = Field(...,description="Unique product id")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponseSchema = Field(...,description="Product category details")


    class Config:
        from_attributes=True

class ProductListResponseSchema(BaseModel):
    product: list[ProductResponseSchema]
    total: int = Field(...,description="Total product count")
