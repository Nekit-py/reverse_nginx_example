from fastapi import APIRouter


foo_router = APIRouter()


@foo_router.get("/foo_index")
async def index():
	return {"message": "Hello from foo index!"}


@foo_router.get("/some_foo_url")
async def some_url():
	return {"message": "Hello from some_foo_url!"}


@foo_router.get("/foo")
async def foo():
	return {"message": "Hello from foo!"}