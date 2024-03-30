from fastapi import FastAPI
from database import Base, engine
from user.user_router import router

Base.metadata.create_all(bind=engine)

tags_metadata = [{
    "name":"Users"
}]
app = FastAPI(openapi_tags=tags_metadata)
app.include_router(router)

@app.get("/healthcheck")
def healthcheck():
    return {"Status":"Up"}
