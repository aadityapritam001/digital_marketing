import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from  app.router  import router


app = FastAPI()

app.include_router(router)

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")


if __name__=='__main__':
    uvicorn.run("main:app", host="localhost", port=5050, reload=True)
