from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.db.db_connections import Base
from app.db.db_connections import engine
from fastapi.middleware.cors import CORSMiddleware

dev_mode = FastAPI()

origins = [
    'http://192.168.0.103:8000'
]

dev_mode.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,           
    allow_methods=["*"],              
    allow_headers=["*"], 
)

@dev_mode.get('/')
def root():
    return {'message': 'Test successful'}

dev_mode.include_router(auth_router)
Base.metadata.create_all(bind=engine)