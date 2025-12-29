from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- 1. DATA MODEL ---
class Item(BaseModel):
    id: int
    name: str
    quantity: int

# --- 2. DATABASE (List) ---
inventory = []

# --- 3. ENDPOINTS ---

@app.post("/items", status_code=201)
def create_item(item: Item):
    inventory.append(item)
    return {"message": "Item added", "item": item}

@app.get("/items")
def get_all_items():
    return inventory

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in inventory:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for i, saved_item in enumerate(inventory):
        if saved_item.id == item_id:
            inventory[i] = updated_item
            return {"message": "Item updated", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, saved_item in enumerate(inventory):
        if saved_item.id == item_id:
            inventory.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")