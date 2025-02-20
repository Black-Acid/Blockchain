import pydantic as pdt


class BooksPostRequest(pdt.BaseModel):
    title: str
    author: str
    rating: int