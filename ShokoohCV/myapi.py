from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


inventory = {

}


@app.get("/")
def home():
    return {"data": "test"}


@app.get("/test")
def hello():
    return {"data": "test2"}


@app.post("/test-post/{item_id}")
def hello_post(item_id: int, item: Item):
    if item_id in inventory:
        return {"data": "not found"}

    inventory[item_id] = item
    return inventory[item_id]


@app.get("/get-item/{item_id}")
def get_item_by_id(item_id: int):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item_by_name(name: str = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        return {"data": "not found"}


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in inventory:
        return {"data": "not found"}

    inventory[item_id].update(item)
    return inventory[item_id]
