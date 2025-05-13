from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#import OAuth2PasswordBearer tells peoplw whwere to send their tokens to, OAuth2PasswordRequestForm helps us to get login form data which is username and password
from jose import jwt, JWTError
# Import jwt to encode and decode jwts  JWTError is raised when the token is invalid or expired
from datetime import datetime, timedelta
# set when token expires
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
