from pydantic import BaseModel


class VideoConfigurationBase(BaseModel):
    sample_1: str


class VideoConfigurationCreate(VideoConfigurationBase):
    pass


class VideoConfigurationUpdate(VideoConfigurationBase):
    pass


class VideoConfigurationInDb(VideoConfigurationBase):
    pass
