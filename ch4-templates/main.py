from fastapi import FastAPI
import uvicorn
import fastapi_chameleon
from views import home, account, packages


app = FastAPI()

def main():
        configure()
        uvicorn.run("main:app", host="localhost",
        port=8000, reload=True)

def configure():
    configure_templates()
    configure_routes()
      
def configure_templates():
    fastapi_chameleon.global_init('templates')
def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)

if __name__ == "__main__":
        main()
else:
    configure()

