from typing import List

from pydantic import BaseModel, Field

"""
ex:
{
  "ppodIntent": {
    "ppodIntentName": "9 digit ISP Name",
    "refCpodIntentName": "9 digit ISP Name",
    "refBuhmName": "Philadelphia",
    "refHubName": "GAL1",
    "refDaasIntentNames": [
      "9 digit ISP Name"
    ]
  },
  "leafUplink": {
    "leafA": {
      "lag": {
        "ipv4": {
          "local": "string",
          "remote": "string",
          "subnet": "string"
        },
        "ipv6": {
          "local": "string",
          "remote": "string",
          "subnet": "string"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": "string"
    },
    "leafB": {
      "lag": {
        "ipv4": {
          "local": "string",
          "remote": "string",
          "subnet": "string"
        },
        "ipv6": {
          "local": "string",
          "remote": "string",
          "subnet": "string"
        }
      },
      "ethernetInterfaces": [
        {
          "localInterface": "string",
          "remoteInterface": "string"
        }
      ],
      "remoteHost": "string"
    }
  },
  "dhcpServers": {
    "ipv4": [
      "string"
    ],
    "ipv6": [
      "string"
    ]
  },
  "vault": {
    "cmSharedSecret": {
      "path": "string",
      "lastUpdated": "string"
    },
    "ripKey": {
      "path": "string",
      "lastUpdated": "string"
    }
  },
  "maggConnections": {
    "ethernetInterfaces": [
      {
        "localInterface": "string",
        "remoteInterface": "string"
      }
    ]
  },
  "custIpScopeConfiguration": {
    "vrfIPScopes": {
      "vrf": [
        {
          "vrfType": "",
          "cm_v4_net": [
            "100.75.170.0/26"
          ],
          "cm_v6_net": [
            "2001:558:40a1::/64"
          ]
        },
        {
          "vrfType": "",
          "cpe_v4_net": [
            "68.35.2.0/23",
            "68.35.30.0/23",
            "21.60.9.0/24",
            "21.60.21.0/24"
          ],
          "cpe_v6_net": [
            "2001:558:6032::/64",
            "2603:27c0:8800::/40"
          ]
        }
      ],
      "anIpscopes": {
        "cm_scope_v4_net": [
          "100.75.170.0/26"
        ],
        "cm_scope_v6_net": [
          "2001:558:40a1:e::/64"
        ],
        "cpe_scope_v4_net": [
          "68.35.2.0/23",
          "68.35.30.0/23"
        ],
        "cpe_scope_v6_net": [
          "2001:558:6032:e::/64"
        ],
        "mta_scope_v4_net": [
          "21.60.9.0/24",
          "21.60.21.0/24",
          "21.60.139.0/24"
        ],
        "mta_scope_v6_net": [
          "2001:558:800a:e::/64"
        ],
        "stb_scope_v6_net": [
          "2603:27c0:8800::/40"
        ],
        "resi_pd_scope_v6_net": [
          "2601:7c0:c800::/40"
        ]
      }
    }
  },
  "refScnProfileName": "Partner East"
}
"""


class PpodIntent(BaseModel):
    ppodIntentName: str
    refCpodIntentName: str
    refBuhmName: str
    refHubName: str
    refDaasIntentNames: List[str]


class Ip(BaseModel):
    local: str
    remote: str
    subnet: str


class Lag(BaseModel):
    ipv4: Ip
    ipv6: Ip


class EthernetInterfaces(BaseModel):
    localInterface: str
    remoteInterface: str


class Leaf(BaseModel):
    lag: Lag
    ethernetInterfaces: List[EthernetInterfaces]
    remoteHost: str


class LeafUplink(BaseModel):
    leafA: Leaf
    leafB: Leaf


class DhcpServers(BaseModel):
    ipv4: List[str]
    ipv6: List[str]


class CmSharedSecret(BaseModel):
    path: str
    lastUpdated: str


class RipKey(BaseModel):
    path: str
    lastUpdated: str


class Vault(BaseModel):
    cmSharedSecret: CmSharedSecret
    ripKey: RipKey


class MaggConnections(BaseModel):
    ethernetInterfaces: List[EthernetInterfaces]


class AnIpscopes(BaseModel):
    cm_scope_v4_net: List[str]
    cm_scope_v6_net: List[str]
    cpe_scope_v4_net: List[str]
    cpe_scope_v6_net: List[str]
    mta_scope_v4_net: List[str]
    mta_scope_v6_net: List[str]
    stb_scope_v6_net: List[str]
    resi_pd_scope_v6_net: List[str]


class Vrf(BaseModel):
    vrfType: str = Field(None)
    cpe_v4_net: List[str] = Field(None)
    cpe_v6_net: List[str] = Field(None)
    cm_v4_net: List[str] = Field(None)
    cm_v6_net: List[str] = Field(None)


class VrfIPScopes(BaseModel):
    vrf: List[Vrf]
    anIpscopes: AnIpscopes


class CustIpScopeConfiguration(BaseModel):
    vrfIPScopes: VrfIPScopes


class PpodIntentBase(BaseModel):
    ppodIntent: PpodIntent
    leafUplink: LeafUplink
    dhcpServers: DhcpServers
    vault: Vault
    maggConnections: MaggConnections
    custIpScopeConfiguration: CustIpScopeConfiguration
    refScnProfileName: str


class PpodIntentCreate(PpodIntentBase):
    pass


class PpodIntentUpdate(PpodIntentBase):
    pass


class PpodIntentInDb(PpodIntentBase):
    pass
