from enum import Enum
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/",description="this our first route")
async def root():
  return{"message": "Hello world!"}


@app.post("/")
async def post():
  return{"message": "Hello world from post route !"}


@app.put("/")
async def put():
  return{"message": "Hello world from put route !"}


@app.get("/users")
async def list_users():
  return{"message": "List users route !"}

@app.get("/users/me")
async def get_current_user():
  return{"message": 'this is the current user'}


@app.get("/users/{user_id}")
async def get_user(user_id : str):
  return{"user_id": user_id}



class FoodEnum(str, Enum):
  fruits = "fruits"
  vegetables = "vegetables"
  dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
  if food_name == FoodEnum.vegetables:
    return{'Food_name':food_name , "message":"you are healthy"}
  
  if food_name.value == 'fruits':
    return{'Food_name':food_name , "message":"you are still healthy, but like sweet things"}
  
  return{'Food_name':food_name , "message":"wtf"}


fake_items_db = [{"item_name" : "Foo"},{"item_name" : "Bar"},{"item_name" : "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0,limit: int = 10):
  return fake_items_db[skip: skip+ limit]



@app.get("/items/{item_id}")
async def get_item(item_id:str , q:Optional[str] = None , short: bool = False):
  item = {'item_id' : item_id}
  if q:
    item.update({ "quary" : q})

  if not short:
    item.update({"description" : "This is a long description"})
  return item