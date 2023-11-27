#Imports
from fastapi import FastAPI, Header, Response
from typing import Optional
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED


#App usage
app = FastAPI()

'''
Api usage
'''

@app.post("/login")
def login(authorization: Optional[str] = Header(None)) -> Response:
    if not authorization == "kishore":
        return Response(status_code=HTTP_401_UNAUTHORIZED)
    return Response(status_code=HTTP_200_OK)
