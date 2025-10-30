from fastapi import FastAPI
from routers.userRoute import router as  userRoute
from routers.candidatRoute import router as  candidatRoute
from routers.offreRoute import router as  offreRoute
from routers.matchingRoute import router as  matchingRoute

ROUTERS = [
    userRoute,
    candidatRoute,
    offreRoute,
    matchingRoute
]

def include_routes(app: FastAPI, api_prefix: str = "/api"):
    for router in ROUTERS:
        app.include_router(router, prefix=api_prefix)
