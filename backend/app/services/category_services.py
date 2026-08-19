from sqlalchemy.orm import Session
from typing import List
from ..repositories.category_repository import CategoryRepository
from ..schemas.category import CategoryResponseSchema, CategoryCreateSchema
from fastapi import HTTPException, status


class CategoryServices:
    def __init__(self, db: Session):
        self.repository=CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponseSchema]:
        categories=self.repository.get_all()
        return [CategoryResponseSchema.model_validate(cat) for cat in categories]


    def get_category_by_id(self, category_id: int)-> CategoryResponseSchema:
        category=self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{category_id} category not found")

        return CategoryResponseSchema.model_validate(category)


    def create_categroy(self, category_data: CategoryCreateSchema) -> CategoryResponseSchema:
        category=self.repository.create(category_data)
        return CategoryResponseSchema.model_validate(category)