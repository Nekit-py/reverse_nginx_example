from fastapi import APIRouter


bar_router = APIRouter()


@bar_router.get("/bar_index")
async def index():
	return {"message": "Hello from bar index!"}


@bar_router.get("/some_bar_url")
async def some_url():
	return {"message": "Hello from some_bar_url!"}


@bar_router.get("/bar")
async def bar():
	return {"message": "Hello from bar!"}