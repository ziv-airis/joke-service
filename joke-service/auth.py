import json
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

file = open('../accounts.json');
accounts = json.load(file);
class Auth(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.headers.get('authorization') not in accounts: 
            return JSONResponse(status_code=403, content={'error': 'Invalid request!'})
        else:
            request.state.account = accounts[request.headers.get('authorization')]["role"]
            return await call_next(request)
