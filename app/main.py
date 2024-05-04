from fastapi import FastAPI
from app.src.dbsetup.dbsetup import Base,session,engine
from app.src.routes.views import route
import uvicorn

def get_application():
    application=FastAPI()
    Base.metadata.create_all(bind=engine)
    application.include_router(route)
    return application

if __name__=="__main__":
    uvicorn.run(get_application())

