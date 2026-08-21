from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: int
    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the category")
    slug: str = Field(..., min_length=5, max_length=100,
                      description="URL - friendly category name")

class CategoryCreateSchema(CategoryBase):
    pass



class CategoryResponseSchema(CategoryBase):
    id: int = Field(...,description="The unique id of the category")


    class Config:
        from_attributes=True