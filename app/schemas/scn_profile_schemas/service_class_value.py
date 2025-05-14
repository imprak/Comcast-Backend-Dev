"""
ex:
{
  "serviceClassValue": {
    "serviceClassValueName": "East",
    "refServiceClassName": "East"
  },
  "config": {
    "applicationId": 0,
    "direction": "Upstream",
    "maxConcatenatedBurst": 0,
    "maxTrafficBurst": 0,
    "maxTrafficRate": 0,
    "maximumBuffer": 0,
    "minReservedPacket": 0,
    "multiplierBytesRequested": 0,
    "multiplierContentionRequestWindow": 0,
    "peakTrafficRate": 0,
    "priority": 0,
    "tosAndMask": "",
    "tosOrMask": "",
    "yangExt": {
      "ccapHarmonic": {
        "isDefaultMinReservedPacket": true
      }
    }
  }
}

"""

from pydantic import BaseModel


class ServiceClassValueBase(BaseModel):
    sample_1: str


class ServiceClassValueCreate(ServiceClassValueBase):
    pass


class ServiceClassValueUpdate(ServiceClassValueBase):
    pass


class ServiceClassValueInDb(ServiceClassValueBase):
    pass
