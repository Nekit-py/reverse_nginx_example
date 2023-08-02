from fastapi import FastAPI
from routers import bar_router
import uvicorn

app = FastAPI(debug=True)
app.include_router(bar_router, prefix='/bar_service')


if __name__ == '__main__':
	uvicorn.run("main:app",
		host="0.0.0.0",
		port=8000,
		reload=True)