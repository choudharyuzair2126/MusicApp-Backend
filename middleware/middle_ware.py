from fastapi import HTTPException, Header
import jwt


def auth_middleware(auth_token = Header()):
    try:
        #get user token
        if not auth_token:
            raise HTTPException(status_code = 401, detail = "No auth token, access denied!")
        #decode token
        verified_token = jwt.decode(auth_token,'password_key','[HS256]')
        if not verified_token:
            raise HTTPException(status_code = 401, detail = "Invalid auth token, access denied!")
        #get user id from token
        uid = verified_token.get('id')
        return {'uid': uid, 'token': auth_token}
        #get user data from database
    except jwt.PyJWTError:
        raise HTTPException(status_code = 401, detail = "Invalid auth token, access denied!")