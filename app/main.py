from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .auth import auth_router
from .routes.ai import ai_router
from .routes.files import files_router

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL
    allow_credentials=False,
    allow_methods=["*"],  # Or ["POST", "GET"] etc.
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/auth")
app.include_router(ai_router, prefix="/ai")
app.include_router(files_router, prefix="/files")