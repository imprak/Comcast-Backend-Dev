"""
ex:
{
  "serviceClassQos": {
    "serviceClassQosName": "East",
    "refServiceClassName": "East"
  },
  "config": {
    "aqmCouplingFactor": 0,
    "asfDirection": "upstream",
    "asfPriority": 0,
    "classicSfScn": "",
    "dataRateUnitSetting": 0,
    "latencySfScn": "",
    "lowLatencyAsf": "",
    "maxAggregateTrafficRate": 0,
    "maxTrafficBurst": 0,
    "minReservedPacket": 0,
    "minReservedRate": 0,
    "peakTrafficRate": 0,
    "qpEnable": "",
    "qpDrainRateExponent": 0,
    "qpLatencyThreshold": 0,
    "qpQueuingScoreThreshold": 0,
    "schedulingWeight": 0
  }
}

"""

from pydantic import BaseModel


class ServiceClassQosBase(BaseModel):
    sample_1: str


class ServiceClassQosCreate(ServiceClassQosBase):
    pass


class ServiceClassQosUpdate(ServiceClassQosBase):
    pass


class ServiceClassQosInDb(ServiceClassQosBase):
    pass
