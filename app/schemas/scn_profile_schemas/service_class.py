"""
ex:
{
  "serviceClassName": "East"
}
"""

from pydantic import BaseModel


class ServiceClassBase(BaseModel):
    serviceClassName: str


class ServiceClassCreate(ServiceClassBase):
    pass


class ServiceClassUpdate(ServiceClassBase):
    pass


class ServiceClassInDb(ServiceClassBase):
    pass
