from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Dict
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
class SOSRequest(BaseModel):
  message:str
#user sends a message
class SOSEvent(BaseModel):
  message:str
  timestamp:str
#what is stored and returned
sos_logs: Dict[str, List[Dict]] = {}
#dictionary stores sos logs fpr each user
@app.post("/sos")
def send_sos(sos: SOSRequest, username: str = Depends(get_current_user)):
  event = {
    "message" : sos.message
    "timestamp" : datetime.utcnow().isoformat()
  }
