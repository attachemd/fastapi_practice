from fastapi import APIRouter
from fastapi import Response

router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]


@router.get("/")
async def get_all_products():
    data = " ".join(products)
    return Response(
        content=data,
        media_type="text/plain",
        status_code=200,
    )
