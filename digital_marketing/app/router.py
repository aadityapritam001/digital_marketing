from fastapi import Request , status, APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")   


@router.get("/",status_code = status.HTTP_200_OK)
async def home(request: Request):
    return templates.TemplateResponse(request= request ,name="index.html")
