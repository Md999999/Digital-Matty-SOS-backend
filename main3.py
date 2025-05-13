from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List, Dict
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
