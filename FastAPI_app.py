from fastapi import FastAPI
import httpx

app = FastAPI()

async def get_user_data(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
        return response.json()

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    user_data = await get_user_data(user_id)
    return {"user": user_data}