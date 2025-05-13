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
@app.post("/contacts")
#handle posts requests to the function endpoint we want to create new emergency contacts
def add_contact(contact: EmergencyContact, username: str = Depends(get_current_user)):
# it makes sure it is in the emergency contact format hence con:eme 
#username: str = Depends(get_current_user)): gets the  username of the current user
if username not in user_contacts:
    user_contacts[username] = []
user_contacts[username].append(contact)
#checkss if the username which is like the user is in the dictionary user contacts if it isnt then an empty list is madr for the user
#appends the new contact to the list of contacts for the user that has logged in.
return {"message": "Contact has been added"}
#contact has been added message


