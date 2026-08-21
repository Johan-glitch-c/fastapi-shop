from sqlalchemy.orm import Session
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductResponseSchema, ProductCreateSchema, ProductListResponseSchema
from typing import List
from fastapi import HTTPException, status


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)

    def get_all(self) -> List[ProductResponseSchema]:
        products = self.product_repository.get_all()
        product_response=[ProductResponseSchema.model_validate(product) for product in products]
        return ProductListResponseSchema(product=product_response,total=len(products))

    def get_product_by_id(self, product_id: int) -> ProductResponseSchema:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
        return ProductResponseSchema.model_validate(product)

    def get_products_by_category(self, category_id: int) -> ProductResponseSchema:
        category=self.category_repository.get_by_id(category_id)

        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category_id} not found")

        products=self.product_repository.get_by_category(category.id)
        product_response=[ProductResponseSchema.model_validate(product) for product in products]
        return ProductListResponseSchema(product=product_response,total=len(products))


    def create_product(self, product_data: ProductCreateSchema) -> ProductResponseSchema:
        category=self.category_repository.create(product_data)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category with id {category.id} not found")
        product=self.product_repository.create(product_data)
        return ProductResponseSchema.model_validate(product)
