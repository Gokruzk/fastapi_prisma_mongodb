from fastapi import APIRouter, Path
from schema import ResponseSchema
from Routes.user import UserRoutes
from Model.user import User
from passlib.hash import sha256_crypt

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get(path="", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all():
    data = await UserRoutes.get_all()
    return ResponseSchema(detail="Successfully retrieved", result=data)


@router.post(path="", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_user(data: User):
    data.psw = sha256_crypt.encrypt(data.psw)
    await UserRoutes.create(data)
    return ResponseSchema(detail="Successfully created")


@router.get(path="{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_dni(id: str = Path(..., alias="id")):
    data = await UserRoutes.get_by_dni(id)
    return ResponseSchema(detail="Successfully retrieved", result=data)


@router.delete(path="{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_user(id: str = Path(..., alias="id")):
    await UserRoutes.delete(id)
    return ResponseSchema(detail="Successfully deleted")


@router.put(path="{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_user(id: str = Path(..., alias="id"), *, data: User):
    await UserRoutes.update(data, id)
    return ResponseSchema(detail="Successfully updated")
