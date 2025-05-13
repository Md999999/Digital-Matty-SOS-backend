from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#import OAuth2PasswordBearer tells peoplw whwere to send their tokens to, OAuth2PasswordRequestForm helps us to get login form data which is username and password
from jose import jwt, JWTError
# Import jwt to encode and decode jwts  JWTError is raised when the token is invalid or expired
from datetime import datetime, timedelta
# set when token expires

