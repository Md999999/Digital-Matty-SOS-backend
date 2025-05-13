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
  #sos end uppoint to send an sos and notify contacts based on the current user with the get current user event function creates an event with the current time and sos
if username not in sos_logs:
  sos_logs[username] = []
  #checks if the username is in soslogs dixtionary if not it creates a new list for it
sos_logs[username].append(event)
#the event is appended for the current user which means it saves the event to the user log

