from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Animal(BaseModel):
    name: str
    nickname: str
    is_venomous: bool
    care_cost: float
    count: int
    continent: str

zoo = []

@app.post("/add_animal/")
async def add_animal(animal: Animal):
    zoo.append(animal)
    return {"message": "Animal added successfully"}

@app.get("/get_animals/")
async def get_animals():
    return zoo

@app.get("/get_venomous_care_cost/")
async def get_venomous_care_cost():
    cost = sum(animal.care_cost * animal.count for animal in zoo if animal.is_venomous)
    return {"venomous_care_cost": cost}

@app.get("/get_african_animals_count/")
async def get_african_animals_count():
    count = sum(animal.count for animal in zoo if animal.continent.lower() == "africa")
    return {"african_animals_count": count}


import requests

BASE_URL = "http://127.0.0.1:8000"

def add_animal(animal):
    response = requests.post(f"{BASE_URL}/add_animal/", json=animal)
    return response.json()

def get_animals():
    response = requests.get(f"{BASE_URL}/get_animals/")
    return response.json()

def get_venomous_care_cost():
    response = requests.get(f"{BASE_URL}/get_venomous_care_cost/")
    return response.json()

def get_african_animals_count():
    response = requests.get(f"{BASE_URL}/get_african_animals_count/")
    return response.json()

animals = [
    {
        "name": "Lion",
        "nickname": "Leo",
        "is_venomous": False,
        "care_cost": 500.0,
        "count": 3,
        "continent": "Africa"
    },
    {
        "name": "Cobra",
        "nickname": "Naga",
        "is_venomous": True,
        "care_cost": 300.0,
        "count": 5,
        "continent": "Asia"
    },
    {
        "name": "Elephant",
        "nickname": "Dumbo",
        "is_venomous": False,
        "care_cost": 1000.0,
        "count": 2,
        "continent": "Africa"
    },
    {
        "name": "Frog",
        "nickname": "Jumpy",
        "is_venomous": True,
        "care_cost": 50.0,
        "count": 10,
        "continent": "South America"
    }
]

for animal in animals:
    print(add_animal(animal))

print("\nСписок тварин у зоопарку:")
print(get_animals())

print("\nВартість догляду за отруйними тваринами:")
print(get_venomous_care_cost())

print("\nКількість африканських тварин:")
print(get_african_animals_count())
