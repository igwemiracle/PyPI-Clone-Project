import fastapi
from fastapi_chameleon import template
from views.home import router


@router.get("/account")
def index():
    pass


@router.get("/account/register")
def register():
    pass


@router.get("/account/login")
def login():
    pass


@router.get("/account/logout")
def logout():
    pass
