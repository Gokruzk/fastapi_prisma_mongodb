from Model.user import User
from Config.db import conn
from bson import ObjectId


class UserRoutes:
    @staticmethod
    async def get_all():
        return await conn.prisma.user.find_many()

    @staticmethod
    async def create(user: User):
        return await conn.prisma.user.create({
            "username": user.username,
            "email": user.email,
            "psw": user.psw
        })

    @staticmethod
    async def get_by_dni(id: str):
        return await conn.prisma.user.find_first_or_raise(where={"id": id})

    @staticmethod
    async def delete(id: str):
        return await conn.prisma.user.delete(where={"id": id})

    @staticmethod
    async def update(user: User, id: str):
        return await conn.prisma.user.update(data={
            "username": user.username,
            "email": user.email,
            "psw": user.psw
        },
            where={"id": id})
