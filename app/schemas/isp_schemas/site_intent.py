"""
ex:
{
  "siteIntent": {
    "siteIntentName": "9 digit ISP name",
    "refBuhmName": "Philadelphia",
    "refHubName": "GAL1",
    "refCpodIntentNames": "9 digit ISP Name",
    "refHaggIntentNames": "9 digit ISP Name"
  },
  "csvIpOob": "",
  "ipAllocation": {
    "comcastRouteable": {
      "ipv4": [
        "string"
      ],
      "ipv6": [
        "string"
      ]
    },
    "partnerInternal": {
      "ipv4": [
        "string"
      ],
      "ipv6": [
        "string"
      ]
    },
    "internetRouted": {
      "ipv4": [
        "string"
      ],
      "ipv6": [
        "string"
      ]
    }
  }
}
"""

from typing import List

from pydantic import BaseModel, Field


class SiteIntent(BaseModel):
    siteIntentName: str
    refBuhmName: str
    refHubName: str
    refCpodIntentNames: str
    refHaggIntentNames: str


class Ip(BaseModel):
    ipv4: List[str]
    ipv6: List[str]


class IpAllocation(BaseModel):
    comcastRouteable: Ip
    partnerInternal: Ip
    internetRouted: Ip


class SiteIntentBase(BaseModel):
    siteIntent: SiteIntent
    csvIpOob: str = Field(None)
    ipAllocation: IpAllocation


class SiteIntentCreate(SiteIntentBase):
    pass


class SiteIntentUpdate(SiteIntentBase):
    pass


class SiteIntentInDb(SiteIntentBase):
    pass
