from datetime import datetime
from ..database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Text, Integer, String, Float, DateTime, ForeignKey, Column


class Product(Base):
    __tablename__ = "products"

    id= Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True, nullable=False)
    category_id=Column(Integer,ForeignKey('categories.id'), nullable=False)
    price=Column(Float, nullable=False)
    description=Column(Text)
    created_at=Column(DateTime, default=datetime.now())
    image_url=Column(String)

    category=relationship('Category', back_populates='products')


    def _repr_(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"