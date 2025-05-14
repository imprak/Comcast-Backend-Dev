from pydantic import BaseModel


class SpectrumRecommendationBase(BaseModel):
    sample_1: str


class SpectrumRecommendationCreate(SpectrumRecommendationBase):
    pass


class SpectrumRecommendationUpdate(SpectrumRecommendationBase):
    pass


class SpectrumRecommendationInDb(SpectrumRecommendationBase):
    pass
