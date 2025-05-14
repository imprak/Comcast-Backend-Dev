from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import (
    isp_endpoints,
    scn_profile_endpoints,
    osp_config_endpoints,
    osp_activation_endpoints,
)

app = FastAPI(title="Comcast-Backend-Dev")

app.include_router(isp_endpoints.router)
app.include_router(scn_profile_endpoints.router)
app.include_router(osp_config_endpoints.router)
app.include_router(osp_activation_endpoints.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse(url="/docs")


# For local test
# import uvicorn
#
# uvicorn.run(app)
