from fastapi import APIRouter, HTTPException
from models.user import User
from config.db import connection
from schemas.user import userEntity,UsersEntity
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
    return UsersEntity(connection.local.user.find())

@user.get('/active_users')
async def get_active_users():
    return UsersEntity(connection.local.user.find({"isactive": True}))

@user.get('/{id}')
async def findone_user(id):
    return userEntity(connection.local.user.find_one({"_id": ObjectId(id)}))

@user.post('/new_user')
async def create_user( user:User ):
    connection.local.user.insert_one(dict(user))
    return UsersEntity(connection.local.user.find())

@user.put('/{id}')
async def update_user(id,user:User):
    connection.local.user.find_one_and_update({"_id": ObjectId(id)},{
        "$set" : dict(user)
    })
    return userEntity(connection.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return userEntity(connection.local.user.find_one_and_delete({"_id":ObjectId(id)}))