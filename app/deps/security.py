from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status


security = HTTPBasic()


class Security:
    def __call__(self, credentials: HTTPBasicCredentials = Depends(security)):
        if credentials.username is None or credentials.password is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Incorrect username or password",
            )

        if credentials.username != "admin":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )

        return credentials.username
