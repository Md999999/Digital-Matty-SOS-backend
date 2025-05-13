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
