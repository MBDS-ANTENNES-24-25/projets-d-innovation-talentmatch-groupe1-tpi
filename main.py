from fastapi import FastAPI
from core.database import initiate_database
from routers import include_routes
app = FastAPI()


@app.on_event("startup")
async def start_db():
    await initiate_database()
    print("")


# importation des routes
include_routes(app) 

@app.get("/")
def read_root():
    return {"Hello": "World"}

