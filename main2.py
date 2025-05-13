from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import BaseModel
from typing import List
#libraries for jwt seperate from the userauthentication to make it cleaner but its at end of code 
class EmergencyContact(BaseModel):
    name: str
    phone: str
    relationship: str
#pydantic creates the class emergency contact to have values like name phone and relation
#pydantic makes sure the input has to match the structure
user_contacts = {}
#stores user contacts in the dictionary
