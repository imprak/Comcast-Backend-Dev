from pydantic import BaseModel


class ActivateFieldRpdBase(BaseModel):
    sample_1: str


class ActivateFieldRpdCreate(ActivateFieldRpdBase):
    pass


class ActivateFieldRpdUpdate(ActivateFieldRpdBase):
    pass


class ActivateFieldRpdInDb(ActivateFieldRpdBase):
    pass
