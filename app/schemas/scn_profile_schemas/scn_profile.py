"""
ex:
{
  "scnProfileName": "Partner East",
  "version": "",
  "serviceClassValues": [
    {
      "refServiceClassValueName": "East"
    }
  ],
  "serviceClassQosValues": [
    {
      "refServiceClassQosName": "East"
    }
  ]
}
"""

from typing import List
from pydantic import BaseModel, Field


class ServiceClassValues(BaseModel):
    refServiceClassValueName: str


class ServiceClassQosValues(BaseModel):
    refServiceClassQosName: str


class ScnProfileBase(BaseModel):
    scnProfileName: str
    version: str = Field(None)
    serviceClassValues: List[ServiceClassValues]
    serviceClassQosValues: List[ServiceClassQosValues]


class ScnProfileCreate(ScnProfileBase):
    pass


class ScnProfileUpdate(ScnProfileBase):
    pass


class ScnProfileInDb(ScnProfileBase):
    pass
