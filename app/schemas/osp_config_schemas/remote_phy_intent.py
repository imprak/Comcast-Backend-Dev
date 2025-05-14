from pydantic import BaseModel


class RemotePhyIntentBase(BaseModel):
    sample_1: str


class RemotePhyIntentCreate(RemotePhyIntentBase):
    pass


class RemotePhyIntentUpdate(RemotePhyIntentBase):
    pass


class RemotePhyIntentInDb(RemotePhyIntentBase):
    pass
