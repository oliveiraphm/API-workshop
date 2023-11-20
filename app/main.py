from fastapi import FastAPI 
from typing import List, Dict, Any

from .routers import router


app = FastAPI()

app.include_router(router)