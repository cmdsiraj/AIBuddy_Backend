from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from .. import models, database
from ..schemas import MessageIn, MessageOut
from ..ai.Agent_main import getResponse

# Config
SECRET_KEY = "328()12dfa37^34*dhcbds"
ALGORITHM = "HS256"

# Security scheme
security = HTTPBearer()

# Decode JWT
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get current user from token
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(database.get_db)
):
    token = credentials.credentials
    payload = decode_access_token(token)

    username: str = payload.get("sub")  # type: ignore
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

# Router setup
ai_router = APIRouter()

@ai_router.post("/chat", response_model=MessageOut)
def chat(
    data: MessageIn,
    current_user: models.User = Depends(get_current_user)
):
    try:
        response = getResponse(data.message)
        if response:
            return {
                "role": "Agent",
                "content": response
            }
        else:
            raise HTTPException(status_code=500, detail="Unexpected error has occurred.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
