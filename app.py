import uvicorn
from fastapi import Cookie, Response, FastAPI, Body
from typing import Optional

app = FastAPI()


@app.post("/set_cookie")
async def set_cookie(resp: Response, uname: str = Body()):
    resp.set_cookie(key="username", value=uname)
    return {"message": f"cookie set with value {uname}"}


@app.get("/peek_cookie")
async def peek_cookie(username: Optional[str] = Cookie(None)):
    return {"cookie_value": username}


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True, debug=True)
