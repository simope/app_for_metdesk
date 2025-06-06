from fastapi import APIRouter


router = APIRouter()

"Simple route"
@router.get("/knock")
def knock():
    return {"message": "Who's there?"}

