from sqlalchemy.orm import Session, joinedload

from ..models.product import Product
from ..schemas.product import ProductCreateSchema
from typing import Optional,List


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Product]:
        return self.db.query(Product).options(joinedload(Product.category).all())


    def get_by_id(self, product_id: int) -> Product:
        return self.db.query(Product).options(joinedload(Product.category)).filter(Product.id == product_id).first()

    def get_by_category(self, category_id: int) -> Product:
        return self.db.query(Product).optionsjoinedload(Product.category).filter(Product.category_id == category_id).all()


    def create(self,product_data: ProductCreateSchema) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product


    def get_multiple_by_ids(self,product_ids: List[int]) -> List[Product]:
        return self.db.query(Product).options(joinedload(Product.category)).filter(Product.id.in_(product_ids)).all()


