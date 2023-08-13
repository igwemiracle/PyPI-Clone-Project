from fastapi_chameleon import template
from fastapi import APIRouter


router = APIRouter()


@router.get("/")
@template(template_file="home/index.pt")
def index(user: str = "annonymous"):
    return {
        "username": user
    }


@router.get("/about/")
def about():
    pass
