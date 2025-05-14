from pydantic import BaseModel


class ActivateShelfRpdBase(BaseModel):
    sample_1: str


class ActivateShelfRpdCreate(ActivateShelfRpdBase):
    pass


class ActivateShelfRpdUpdate(ActivateShelfRpdBase):
    pass


class ActivateShelfRpdInDb(ActivateShelfRpdBase):
    pass
