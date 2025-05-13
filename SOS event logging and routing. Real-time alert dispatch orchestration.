from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Dict
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
#libraries for jwt seperate from the userauthentication to make it cleaner but its at end of code 
app = FastAPI()
SECRET_KEY = "mysecret" #used to sign and verify tokens should be secret
ALGORITHM = "HS256" #to encrypt jwt
ACCESS_TOKEN_EXPIRE_MINUTES = 30 #sets token to expire after 30 mins
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#user will get token from the login section looks for a token in the request header
users = {}
#to store username and passowrds it is a dictionary and empty
@app.post("/register")
def register(form_data: OAuth2PasswordRequestForm = Depends()):
#register section is made ,OAuth2PasswordRequestForm to collects the form data username and password)
    if form_data.username in users:
        raise HTTPException(status_code=400, detail="User exists")
#checks if the username already is there if it is an error is made
    users[form_data.username] = form_data.password
    return {"message": "User made"}
#checks if its not taken the username if it isn't then a user is created
 @app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
#uses username and password-login section
    user_pass = users.get(form_data.username)
    if not user_pass or user_pass != form_data.password:
        raise HTTPException(status_code=400, detail="Wrong credentials")
#checks if the username is there and the password matches if it doesnt then its an error
    payload = {
        "sub": form_data.username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
#jwt payload is made sub is the username exp is when the token expires
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
# JWT is encoded using the payload,secret key and algorithm
    return {"access_token": token, "token_type": "bearer"}
#token is returned in a normal way so the user knows how to use it
def get_current_user(token: str = Depends(oauth2_scheme)):
    #used to protect routes pulls the token from requests using oauth2
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
        #Decode the token it checks the signature and expiry gets the username from payload and return it
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
# error is made when token is expired 
@app.get("/protected")
def protected_route(username: str = Depends(get_current_user)):
#protected section is made only people with actual valid token can to get this stage
    return {"message": f"Hello, {username}! You're authenticated"}
#youre authenticated message is returned along with your username this is a formatted string like it is done in C# f at the beginning
#is like python will replace username with an actual username


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
@app.get("/contacts", response_model=List[EmergencyContact])
# get requests for the conacts endpoont
def get_contacts(username: str = Depends(get_current_user)):
#gets current user gets contacts for the current user by checking for their username which goes hand in hand with yhe user
return user_contacts.get(username, [])
#returns a list of contacts for the user fron the dictonary for the checked username no contacts are found then its empty.


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
