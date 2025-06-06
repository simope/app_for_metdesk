from fastapi import APIRouter


router = APIRouter()


@router.get("/knock")  # Simple route
def knock():
    return {"message": "Who's there?"}
