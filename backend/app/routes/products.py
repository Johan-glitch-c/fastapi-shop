from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.product import ProductListResponseSchema, ProductResponseSchema
from fastapi import APIRouter, Depends, status
from ..services.product_services import ProductService

router=APIRouter(
    prefix="/api/products",
    tags=["products"]
)


@router.get("",response_model=ProductListResponseSchema, status_code=status.HTTP_200_OK)
def get_products(db:Session=Depends(get_db)):
    service=ProductService(db)
    return service.get_all()

@router.get("/{product_id}", response_model=ProductResponseSchema, status_code=status.HTTP_200_OK)
def get_product(product_id:int, db: Session = Depends(get_db)):
    service=ProductService(db)
    return service.get_product_by_id(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponseSchema, status_code=status.HTTP_200_OK)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    service=ProductService(db)
    return service.get_products_by_category(category_id)