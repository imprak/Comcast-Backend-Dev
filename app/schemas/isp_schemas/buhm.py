from pydantic import BaseModel


"""
ex:
{
      "buhmType": "Market, Region, Division",
      "buhmName": "Philadelphia",
      "parentBuhmName": "NED"
    }
"""


class BuhmBase(BaseModel):
    buhmType: str
    buhmName: str
    parentBuhmName: str


class BuhmCreate(BuhmBase):
    pass


class BuhmUpdate(BuhmBase):
    pass


class BuhmInDb(BuhmBase):
    pass
